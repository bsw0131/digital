import json
from functools import lru_cache

from dotenv import load_dotenv

from offline_engine import (
    fit_scores,
    make_interview,
    make_plan,
    make_report,
    make_research_guide,
    make_survey,
    recommend_topics,
)
from settings_store import DEFAULT_MODEL, get_ai_settings_private, record_ai_usage, refresh_ai_model

load_dotenv()


def get_online_config() -> dict:
    settings = get_ai_settings_private()
    return {
        "enabled": bool(settings.get("online_ai_enabled")),
        "api_key": settings.get("openai_api_key", ""),
        "model": settings.get("model") or DEFAULT_MODEL,
    }


def has_api_key() -> bool:
    config = get_online_config()
    return bool(config["enabled"] and config["api_key"])


@lru_cache(maxsize=2)
def _cached_online_client(api_key: str):
    from openai import OpenAI

    # 재시도 정책은 아래 호출 계층에서 오류 유형별로 제어한다.
    return OpenAI(api_key=api_key, timeout=60.0, max_retries=0)


def _online_client(config: dict):
    return _cached_online_client(config["api_key"])


def _clean_json_text(text: str) -> str:
    cleaned = (text or "").strip().replace("＇＇＇json", "").replace("＇＇＇", "").replace("```json", "").replace("```", "").strip()
    if cleaned.startswith("[") and "]" in cleaned:
        return cleaned[:cleaned.rfind("]") + 1]
    if cleaned.startswith("{") and "}" in cleaned:
        return cleaned[:cleaned.rfind("}") + 1]
    array_start, array_end = cleaned.find("["), cleaned.rfind("]")
    if array_start >= 0 and array_end > array_start:
        return cleaned[array_start:array_end + 1]
    object_start, object_end = cleaned.find("{"), cleaned.rfind("}")
    if object_start >= 0 and object_end > object_start:
        return cleaned[object_start:object_end + 1]
    return cleaned


def _is_model_error(exc: Exception) -> bool:
    message = str(exc).lower()
    return any(token in message for token in (
        "model_not_found", "model does not exist", "does not exist or you do not have access",
        "not have access to model", "unsupported model",
    ))


def _chat_completion(config: dict, messages: list[dict], max_tokens: int, json_mode: bool = False):
    import time
    from openai import APIConnectionError, APITimeoutError, BadRequestError, InternalServerError, NotFoundError, OpenAIError, PermissionDeniedError, RateLimitError
    client = _online_client(config)

    def create(model: str):
        params = {"model": model, "messages": messages}
        if model.startswith("gpt-5"):
            params["reasoning_effort"] = "none"
        if json_mode:
            params["response_format"] = {"type": "json_object"}
        try:
            response = client.chat.completions.create(**params, max_completion_tokens=max_tokens)
        except BadRequestError as exc:
            message = str(exc).lower()
            if "reasoning_effort" in message:
                params.pop("reasoning_effort", None)
                response = client.chat.completions.create(**params, max_completion_tokens=max_tokens)
            elif "max_completion_tokens" in message or "unsupported parameter" in message:
                params.pop("reasoning_effort", None)
                response = client.chat.completions.create(**params, max_tokens=max_tokens)
            elif json_mode and ("response_format" in message or "json_object" in message):
                params.pop("response_format", None)
                response = client.chat.completions.create(**params, max_completion_tokens=max_tokens)
            else:
                raise
        if not (response.choices[0].message.content or "").strip():
            raise RuntimeError(f"{model} 모델이 빈 응답을 반환했습니다.")
        return response

    model = config["model"]
    transient_errors = (APIConnectionError, APITimeoutError, RateLimitError, InternalServerError)
    last_error = None
    for attempt in range(3):
        try:
            return create(model)
        except transient_errors as exc:
            last_error = exc
            if attempt < 2:
                time.sleep(0.8 * (2 ** attempt))
                continue
        except (NotFoundError, PermissionDeniedError) as exc:
            last_error = exc
            break
        except BadRequestError as exc:
            if not _is_model_error(exc):
                raise
            last_error = exc
            break
        except RuntimeError:
            raise
        except OpenAIError:
            raise
    if isinstance(last_error, transient_errors):
        raise last_error
    new_model = refresh_ai_model(config["api_key"], model, excluded_models={model})
    config["model"] = new_model
    return create(new_model)


def _online_text(system: str, prompt: str, temperature: float = 0.45, max_tokens: int = 3000) -> str:
    config = get_online_config()
    if not (config["enabled"] and config["api_key"]):
        raise RuntimeError("online ai disabled")
    res = _chat_completion(
        config,
        [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        max_tokens,
    )
    return (res.choices[0].message.content or "").strip()


def _online_json_list(system: str, prompt: str, min_items: int = 4, max_items: int = 7) -> list[str]:
    text = _online_text(system, prompt, 0.4, 2400)
    data = json.loads(_clean_json_text(text))
    if isinstance(data, dict):
        data = data.get("items", [])
    if not isinstance(data, list):
        raise ValueError("AI response is not a list")
    items = [str(item).strip() for item in data if str(item).strip()]
    if len(items) < min_items:
        raise ValueError("AI response has too few items")
    return items[:max_items]


QUALITY_RULES = """
너는 대한민국 중·고등학생의 탐구활동을 설계하는 전문 연구 코치다.
답변은 학생이 이해할 수 있는 명료한 한국어로 쓰되, 내용의 깊이는 교사가 수행평가 자료로 활용할 수 있을 정도여야 한다.

모든 답변에 다음 품질 기준을 적용한다.
1. 주제 맞춤성: 어느 주제에도 붙일 수 있는 일반론을 쓰지 말고, 입력된 주제의 핵심 개념과 실제 사례를 반영한다.
2. 수행 가능성: 학교에서 2~4주 안에 자료조사, 설문, 인터뷰, 관찰, 공개 데이터 또는 안전한 간이 실험으로 실행할 수 있어야 한다.
3. 연구 구체성: 조사 대상, 비교 집단, 핵심 변인, 표본 규모, 기간, 측정·기록 방법, 분석 기준 중 해당되는 내용을 수치와 예시로 구체화한다.
4. 학문적 타당성: 주장과 근거를 구분하고, 상관관계를 인과관계로 단정하지 않으며, 예상 결과를 실제 결과처럼 꾸며내지 않는다.
5. 출처 신뢰성: 정부·공공기관·학술기관·공식 통계·전문기관 자료를 우선하고, 출처명·발행일·작성 주체·다른 출처와의 일치 여부를 확인하게 한다.
6. 단계 연결성: 탐구 문제 → 자료 수집 → 분석 → 결론이 같은 핵심 변인과 기준으로 자연스럽게 이어져야 한다.
7. 학생 안전과 윤리: 개인정보, 민감 질문, 위험한 실험, 저작권 침해를 피하고 익명성·동의·출처 표시를 안내한다.
8. 수준 조절: 중학생에게는 낯선 용어를 짧게 풀이하고, 고등학생에게는 변인 통제·표본 편향·한계·후속 연구까지 생각하게 한다.
9. 표현 품질: '조사해 보세요', '다양한 자료를 활용하세요' 같은 막연한 문장 대신 학생이 바로 행동할 수 있는 문장을 쓴다.
10. 정직성: 학생이 제공하지 않은 조사 결과, 수치, 인터뷰 발언, 참고문헌을 절대 만들어내지 않는다.
11. 주제 계약: 답변을 만들기 전에 주제의 핵심 대상·개념, 범위, 비교 조건 또는 변인, 필요한 근거, 적합한 탐구법을 내부적으로 확정하고 모든 단계에서 그대로 유지한다.
12. 방법 적합성: 주제를 개념·원리형, 영향·관계형, 비교형, 개선·설계형, 윤리·판단형 중 하나 이상으로 판별한다. 개념의 참·거짓을 학생 설문으로 증명하지 말고 문헌·사례·반례·모형·안전한 실험을 우선하며, 설문은 이해도나 오개념 확인에만 보조적으로 쓴다.
13. 측정 가능성: '영향', '효과', '만족', '안전' 같은 말을 그대로 두지 말고 관찰 가능한 지표, 응답 기간, 비교 기준으로 바꾼다.
14. 결론 경계: 모은 자료가 답할 수 있는 범위와 답할 수 없는 범위를 구분하고, 예외 사례와 가능한 다른 설명을 반드시 남긴다.
15. 주제 충실도 검사: 출력 전 제목의 핵심어가 탐구 질문, 수집 도구, 분석 기준, 결론 항목에 실제로 등장하는지 확인하고, 하나라도 끊기면 다시 작성한다.
16. 교과 맞춤성: 주제와 관련된 교과 개념 2~4개를 정확히 골라 쉬운 정의와 탐구에서의 역할을 연결한다. 관련 없는 전문 용어를 장식처럼 넣지 않는다.
17. 증거 설계: 세부 질문마다 '무슨 근거가 필요하고, 어디서 어떻게 얻으며, 어떤 표·그래프로 판단할지'가 일대일로 대응해야 한다.
18. 학생 선택 지원: 방법을 나열하는 데 그치지 말고 이 주제에 가장 적합한 주된 방법 1개와 보조 방법을 구분하고, 적합한 이유를 설명한다.
"""


def _weeks_from_duration(value) -> int:
    digits = "".join(ch for ch in str(value or "") if ch.isdigit())
    return int(digits) if digits else 3


def _normalize_recommendation_scores(items: list[dict]) -> list[dict]:
    normalized = []
    for item in items:
        topic = str(item.get("topic") or "").strip()
        if not topic:
            continue
        item["topic"] = topic
        item["fit"] = fit_scores(
            topic,
            item.get("inquiry_type") or "",
            item.get("difficulty") or "중",
            _weeks_from_duration(item.get("duration")),
        )
        normalized.append(item)
    normalized.sort(key=lambda x: (x.get("fit") or {}).get("total", 0), reverse=True)
    return normalized


def recommend(tag: str, detail: str):
    config = get_online_config()
    if not (config["enabled"] and config["api_key"]):
        return {"mode": "offline", "items": recommend_topics(tag, detail)}

    try:
        client = _online_client(config)
        prompt = f"""
{QUALITY_RULES}

학생의 관심 정보
- 선택 태그: {tag or "없음"}
- 직접 입력: {detail or "없음"}

중·고등학생이 실제로 수행할 수 있으면서도 서로 겹치지 않는 탐구주제 15개를 설계하라.

주제 설계 기준:
- 제목만 보아도 '무엇을, 누구에게서/어디에서, 어떤 기준으로 비교·분석하는지' 짐작할 수 있게 한다.
- 단순 현황·선호도·인식 조사에 머물지 말고 원인, 영향, 조건별 차이, 개선안, 윤리 쟁점, 원리 탐구 중 하나 이상을 포함한다.
- 두 관심사가 자연스럽게 연결되면 실제 생활 장면과 공통 변인을 찾아 융합하고, 억지스러우면 관심사별로 나누어 추천한다.
- 개념어가 입력되면 정의·원리·구조·성립 조건·증명 아이디어를 파고드는 질문형 주제를 포함한다.
- 15개 안에서 자료 분석형, 설문·인터뷰형, 관찰·비교형, 안전한 간이 실험형, 해결안 설계형을 균형 있게 섞는다.
- 같은 문장 구조와 비슷한 변인을 반복하지 않는다.
- 먼저 각 후보를 개념·원리형, 영향·관계형, 비교형, 개선·설계형, 윤리·판단형으로 판별하고 그 유형에 맞는 탐구법을 고른다.
- reason에는 추천 이유뿐 아니라 '주제의 핵심어와 범위, 수집할 근거/대상, 핵심 비교·판단 기준, 가능한 분석법, 결론의 한계'를 2~3문장으로 구체적으로 적는다.
- 학생 의견으로 객관적 원리나 사실을 증명하는 주제를 만들지 않는다. 원리형은 문헌·사례·반례·모형·안전한 간이 실험을 우선한다.
- difficulty는 중/중상/상 중 하나, duration은 2주/3주/4주 중 하나로 쓴다.
- fit은 0~100 정수로 작성하되 실제 점수는 서버에서 다시 계산한다.

반드시 아래 키를 가진 JSON 배열만 출력한다. 설명이나 코드블록은 붙이지 않는다.
[
  {{
    "topic": "구체적인 탐구 질문 또는 제목",
    "subject": "관련 교과 1~2개",
    "difficulty": "중|중상|상",
    "inquiry_type": "주된 탐구 방법",
    "duration": "2주|3주|4주",
    "reason": "수행 방법과 분석 기준까지 포함한 구체적 설명",
    "fit": {{
      "data_collection": 0,
      "survey": 0,
      "experiment": 0,
      "school_application": 0,
      "total": 0
    }}
  }}
]
"""
        res = _chat_completion(config, [{"role": "user", "content": prompt}], 7000)
        text = _clean_json_text(res.choices[0].message.content)
        parsed = json.loads(text)
        if isinstance(parsed, dict):
            parsed = parsed.get("items") or parsed.get("topics") or []
        items = _normalize_recommendation_scores(parsed)
        if len(items) < 10:
            raise ValueError("AI response has too few recommendations")
        return {"mode": "online", "items": items[:15]}
    except Exception as exc:
        return {
            "mode": "offline",
            "items": recommend_topics(tag, detail),
            "ai_error": "AI 추천을 생성하지 못해 오프라인 추천으로 전환했습니다.",
            "ai_error_code": type(exc).__name__,
        }


def plan(topic: str):
    try:
        return _online_text(
            QUALITY_RULES,
            f"""
탐구 주제: {topic}

이 주제로 학생이 그대로 실행할 수 있는 탐구계획서를 작성하라.
먼저 제목에서 핵심 대상·개념, 포함/제외 범위, 비교 조건 또는 변인, 필요한 근거를 추출해 '주제 적합성 핵심'으로 4줄 이내에 제시한다. 이후 모든 항목은 그 핵심을 유지하며, 제목보다 넓은 일반적인 학생 인식 조사로 바꾸지 않는다.
주제 유형에 맞는 주된 검증법을 선택하고 설문·인터뷰는 필요한 경우에만 보조 수단으로 둔다. 각 항목은 주제에 맞춘 실제 내용으로 채우고 다음 구조를 지킨다.

1. 탐구 동기
- 학생 생활 또는 사회·교과 맥락과 연결한 3~4문장
- 왜 이 주제를 확인할 가치가 있는지 설명

2. 탐구 문제
- 답을 미리 정하지 않은 핵심 질문 1개
- 핵심 질문을 검증하는 세부 질문 3개
- 각 세부 질문 바로 아래에 [필요 근거] [수집 방법] [분석·판단 기준]을 한 줄씩 대응
- 비교할 독립 변인과 관찰할 종속 변인(해당되는 경우)을 쉬운 말로 표시

3. 예상과 근거
- 예상 결과 1~2개와 그렇게 예상하는 이유
- 예상은 가설이며 실제 결과가 아님을 명시

4. 탐구 대상과 범위
- 조사·관찰 대상, 권장 표본 수, 비교 집단, 기간, 장소, 제외 범위
- 표본을 구하기 어려울 때 가능한 대안

5. 자료 수집 계획
- 주제 핵심어와 교과 개념 2~4개의 쉬운 정의
- 신뢰할 만한 자료 출처 유형 3개와 주제어가 실제로 포함된 검색어 예시 4개
- 설문·인터뷰·관찰·간이 실험 중 적합한 방법, 횟수와 기록 양식
- 개인정보 보호, 동의, 안전 주의점

6. 분석 계획
- 표 또는 그래프 종류와 축에 넣을 값
- 평균, 비율, 빈도, 조건별 비교 중 사용할 방법
- 어떤 결과가 나오면 핵심 질문을 어떻게 해석할지 판단 기준
- 제목의 핵심어 → 질문 → 자료 열 → 그래프 축 → 결론 문장으로 이어지는 '주제 연결 점검표'

7. 일정과 역할
- 3주 기준 주차별 할 일과 산출물
- 개인 탐구와 모둠 탐구 각각의 역할 예시

8. 예상 한계와 보완
- 표본 편향, 측정 오류, 통제하기 어려운 요인 등 예상 한계 2개 이상
- 각 한계를 줄일 현실적인 방법

9. 최종 산출물과 학교 적용
- 보고서에 포함할 표·그래프·사진·부록
- 탐구 결과를 학교생활에 적용할 수 있는 구체적 제안

중학생도 이해할 수 있도록 전문 용어는 괄호로 풀이하되, 고등학생이 사용해도 얕지 않게 작성한다.
""",
            0.38,
            3600,
        )
    except Exception:
        pass
    return make_plan(topic)


def survey(topic: str):
    try:
        return _online_json_list(
            QUALITY_RULES,
            f"""
탐구 주제: {topic}

이 주제의 핵심 질문을 실제로 분석할 수 있는 설문 문항 7개를 설계하라.
먼저 주제가 객관적 원리·개념을 다루는지 판별한다. 그런 주제라면 설문으로 원리의 진위를 증명하려 하지 말고 학생의 사전 이해·대표 오개념·근거 선택·학습 후 변화만 측정하는 보조 설문으로 만든다. 경험·영향·비교 주제라면 제목의 원인 후보, 결과 지표, 대상과 기간을 문항에 직접 반영한다.

조건:
- JSON 문자열 배열만 출력한다.
- 첫 문항은 조사 목적과 익명 응답 안내를 포함한 짧은 안내문으로 만든다.
- 나머지는 응답자 특성 1개, 행동·경험 2개, 원인 또는 영향 2개, 개선안·의견 1개가 되도록 구성한다.
- 각 문항 문자열에 질문, 응답 형식, 선택지를 함께 쓴다.
- 5점 척도는 양 끝 의미를 모두 표시하고, 빈도 문항은 구체적인 기간을 제시한다.
- 한 문항에는 한 가지 내용만 묻고, 유도 질문·이중 부정·모호한 '자주' 표현을 피한다.
- 민감한 개인정보는 묻지 않고 '응답하지 않음' 선택지가 필요한 경우 포함한다.
- 마지막 문항은 선택형 결과를 해석하는 데 도움이 되는 짧은 서술형으로 만든다.
- 각 문항이 탐구의 어떤 변인 또는 판단 기준을 측정하는지 대괄호로 짧게 표시한다.
""",
            min_items=7,
            max_items=7,
        )
    except Exception:
        pass
    return make_survey(topic)


def guide(topic: str):
    try:
        return _online_json_list(
            QUALITY_RULES,
            f"""
탐구 주제: {topic}

학생이 검색부터 분석 준비까지 순서대로 실행할 수 있는 자료조사 가이드 7단계를 작성하라.
1단계에서 제목의 핵심어·포함 범위·제외 범위를 고정하고, 2단계에서 핵심 질문/필요 근거/수집법 연결표를 만들게 한다. 이후 단계마다 제목의 구체적인 핵심어를 다시 사용해 일반론으로 흐르지 않게 한다.

조건:
- JSON 문자열 배열만 출력한다.
- 각 항목은 '단계명 — 할 일 — 기록할 내용/산출물' 형식의 구체적인 실행 문장으로 쓴다.
- 반드시 다음을 포함한다: 주제 범위 고정, 교과 핵심 개념 정의, 주제어가 포함된 검색어 만들기, 공신력 있는 출처 찾기, 출처 신뢰도 확인, 서로 다른 자료 교차 검증, 세부 질문별 수치·사례 추출, 표로 비교 정리, 직접 조사 결과와 연결하기.
- 각 단계에 이 주제에서 실제로 찾아야 할 구체적인 개념·조건·수치·사례를 적고, 다른 주제에도 그대로 쓸 수 있는 표현을 금지한다.
- 정부·공공기관·대학·학술정보·공식 통계 등 주제에 적합한 출처 유형을 구체적으로 제안하되 존재하지 않는 자료명이나 링크를 만들지 않는다.
- 출처 기록 양식(기관/작성자, 제목, 발행일, URL, 확인일)을 안내한다.
- 복사·붙여넣기 대신 자기 말로 요약하고 직접 인용에는 따옴표와 출처를 표시하도록 한다.
- 상반된 자료가 나왔을 때 작성 주체, 조사 시점, 표본, 정의 차이를 비교하게 한다.
""",
            min_items=7,
            max_items=7,
        )
    except Exception:
        pass
    return make_research_guide(topic)


def interview(topic: str):
    try:
        return _online_json_list(
            QUALITY_RULES,
            f"""
탐구 주제: {topic}

학생이 안전하고 자연스럽게 진행할 수 있는 인터뷰 안내와 질문 7개를 작성하라.
주제의 핵심어, 원인·과정, 판단 기준, 반례·예외를 직접 묻도록 설계한다. 개념·원리형이면 관련 교과 교사·전문가와 서로 다른 이해 수준의 학생을 구분하고, 전문가 답변과 학생 이해도 자료의 역할을 섞지 않는다.

조건:
- JSON 문자열 배열만 출력한다.
- 첫 항목은 적합한 인터뷰 대상 2~3유형, 선정 이유, 요청 방법, 예상 시간, 녹음·익명 처리 동의 안내를 포함한다.
- 질문은 쉬운 시작 질문 → 구체적 경험 → 주제의 핵심 과정·원인 → 판단 기준 → 자료조사와 다른 점 → 반례·예외 → 개선 제안 순서로 깊어지게 한다.
- 각 질문이 어느 세부 탐구 질문에 답하기 위한 것인지 [연결: ...]로 표시한다.
- 예/아니오로 끝나지 않는 열린 질문으로 만들고, 각 질문 뒤에 사용할 수 있는 꼬리 질문 1개를 괄호로 넣는다.
- 답을 유도하거나 특정 입장을 전제하지 않는다.
- 학생이 얻은 답을 주제별 코드로 묶고 공통점·차이점·예외 사례를 정리할 수 있도록 마지막 항목에 분석 방법을 포함한다.
- 학교 안에서 만날 수 있는 대상과 외부 전문가의 대체 방법(이메일 서면 인터뷰 등)을 함께 고려한다.
""",
            min_items=7,
            max_items=7,
        )
    except Exception:
        pass
    return make_interview(topic)


def report(topic: str, plan_text: str, log: str):
    try:
        return _online_text(
            QUALITY_RULES,
            f"""
탐구 주제: {topic}

학생의 탐구계획:
{plan_text or "아직 입력되지 않음"}

학생의 메모와 탐구일지:
{log or "아직 입력되지 않음"}

제공된 내용만 근거로 완성도 높은 보고서 초안을 Markdown으로 작성하라.

작성 원칙:
- 학생이 제공하지 않은 수치, 조사 결과, 인터뷰 발언, 출처, 실험 과정을 만들어내지 않는다.
- 정보가 부족한 곳은 ___로 두고 바로 뒤에 [무엇을 입력할지]를 구체적으로 안내한다.
- 첫 부분에 '주제 적합성 핵심'을 두어 최종 제목, 교과 핵심 개념, 포함·제외 범위, 핵심 질문, 필요한 근거, 주된 탐구법을 명시한다.
- 계획서의 탐구 문제와 실제 수집 자료, 분석, 결론이 같은 핵심어·대상·변인·판단 기준으로 일관되게 이어지는지 확인한다.
- 제목보다 넓은 일반론이나 단순 학생 인식으로 주제를 바꾸지 않는다. 개념·원리형 주제에서 설문은 이해도 보조 자료일 뿐 사실의 증거로 쓰지 않는다.
- 결과와 해석을 분리하고, 상관관계를 인과관계로 단정하지 않는다.
- 세부 질문마다 실제 근거가 있는지 '질문-근거-분석-결론 정합성 표'로 점검하고, 근거가 없는 질문은 결론 대신 [추가 조사 필요]로 남긴다.
- 단순 요약이 아니라 결과가 왜 그렇게 나타났는지 가능한 설명과 반대 해석도 제시한다.
- 중학생이 이해할 수 있는 문장으로 쓰되 핵심 개념, 변인, 표본, 한계는 정확하게 표현한다.

필수 목차:
# 탐구 보고서 제목
## 1. 탐구 동기와 목적
## 2. 탐구 문제와 예상
## 3. 이론적 배경
- 핵심 개념 정의와 자료조사 요약
- 실제 출처가 없으면 [출처 추가 필요] 표시
## 4. 탐구 대상과 방법
- 대상·표본·기간·절차·윤리 및 안전
## 5. 탐구 결과
- 자료별 사실 정리
- 넣어야 할 표 또는 그래프의 제목, 열/축 구성 예시
## 6. 결과 분석과 논의
- 핵심 질문에 대한 해석
- 예상과 실제 결과 비교
- 자료 간 공통점·차이점·예외 및 대안 설명
## 7. 결론
- 근거로 말할 수 있는 범위 안의 답
## 8. 한계와 후속 탐구
- 표본, 측정, 자료 신뢰도 한계와 개선 방법
## 9. 학교생활 적용 제안
- 실행 주체, 방법, 기간, 확인 지표가 드러나는 제안
## 10. 참고자료와 부록
- 참고자료 기록 양식과 설문·인터뷰 문항 첨부 안내

마지막에 '제출 전 확인표'를 만들어 근거 없는 문장, 출처 표시, 표·그래프 제목, 개인정보 제거, 맞춤법을 학생이 점검하게 한다.
""",
            0.32,
            4600,
        )
    except Exception:
        pass
    return make_report(topic, plan_text, log)
# === 저토큰 AI 실행 계층 (QR 전용) ===
_COMPACT_SYSTEM = """중·고등학생 탐구 코치다. 주제의 핵심어·범위·근거를 유지하고 2~4주 내 실행 가능하게 쓴다. 사실/의견과 상관/인과를 구분하며 없는 수치·출처는 만들지 않는다. 짧고 구체적인 한국어로 답한다."""
_RESULT_CACHE = {}
_RESULT_CACHE_LIMIT = 128
AI_TOKEN_BUDGETS = {
    "recommend": 1200,
    "plan": 900,
    "guide": 900,
    "survey": 900,
    "interview": 900,
    "report": 1600,
}


def _cache_key(operation: str, config: dict, prompt: str) -> str:
    import hashlib
    key_hash = hashlib.sha256(config["api_key"].encode("utf-8")).hexdigest()[:12]
    prompt_hash = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
    return f"{operation}:{config['model']}:{key_hash}:{prompt_hash}"


def _compact_call(operation: str, prompt: str, max_tokens: int, *, json_mode: bool = False, bypass_cache: bool = False) -> str:
    config = get_online_config()
    if not (config["enabled"] and config["api_key"]):
        raise RuntimeError("online ai disabled")
    key = _cache_key(operation, config, prompt)
    if not bypass_cache and key in _RESULT_CACHE:
        record_ai_usage(operation, config["model"], cache_hit=True)
        return _RESULT_CACHE[key]
    response = _chat_completion(config, [{"role": "system", "content": _COMPACT_SYSTEM}, {"role": "user", "content": prompt}], max_tokens, json_mode=json_mode)
    text = (response.choices[0].message.content or "").strip()
    record_ai_usage(operation, config["model"], response.usage)
    if len(_RESULT_CACHE) >= _RESULT_CACHE_LIMIT:
        _RESULT_CACHE.pop(next(iter(_RESULT_CACHE)))
    _RESULT_CACHE[key] = text
    return text


def _compact_json_data(operation: str, prompt: str, max_tokens: int):
    last_error = None
    for attempt in range(2):
        retry_prompt = prompt
        if attempt:
            retry_prompt += "\n이전 응답이 잘렸거나 JSON 형식이 아니었다. 설명 없이 완전한 JSON 객체 하나만 다시 출력한다."
        try:
            text = _compact_call(operation, retry_prompt, max_tokens, json_mode=True, bypass_cache=bool(attempt))
            return json.loads(_clean_json_text(text))
        except (json.JSONDecodeError, ValueError, TypeError) as exc:
            last_error = exc
    raise last_error or ValueError("AI JSON response could not be parsed")


def _compact_json_list(operation: str, prompt: str, count: int, max_tokens: int = 1500) -> list[str]:
    data = _compact_json_data(operation, prompt, max_tokens)
    if isinstance(data, dict):
        data = data.get("items", [])
    if not isinstance(data, list):
        raise ValueError("AI response is not a list")
    items = [str(item).strip() for item in data if str(item).strip()]
    if len(items) < count:
        raise ValueError("AI response has too few items")
    return items[:count]


def _recommendation_rows(data) -> list[dict]:
    """압축 배열 응답을 기존 화면용 객체로 바꾼다."""
    if isinstance(data, dict):
        data = data.get("items") or data.get("topics") or []
    rows = []
    for item in data if isinstance(data, list) else []:
        if isinstance(item, dict):
            rows.append(item)
        elif isinstance(item, list) and len(item) >= 6:
            rows.append({
                "topic": item[0], "subject": item[1], "difficulty": item[2],
                "inquiry_type": item[3], "duration": item[4], "reason": item[5],
            })
    return rows


def _compact_context(value: str, limit: int) -> str:
    text = "\n".join(line.strip() for line in (value or "").splitlines() if line.strip())
    if len(text) <= limit:
        return text
    head = int(limit * 0.65)
    tail = limit - head
    return text[:head].rstrip() + "\n[…중간 내용 생략…]\n" + text[-tail:].lstrip()


def recommend(tag: str, detail: str):
    config = get_online_config()
    if not (config["enabled"] and config["api_key"]):
        return {"mode": "offline", "items": recommend_topics(tag, detail)}
    prompt = f"""관심사={tag or '없음'}; 세부={detail or '없음'}
서로 다른 실행 가능한 탐구주제 5개를 JSON 객체로만 출력한다.
형식: {{"items":[[제목,교과,난이도,방법,기간,이유], ...]}}. 난이도=중/중상/상, 기간=2주/3주/4주.
제목에 대상·핵심개념·비교/판단기준을 넣고 자료분석·설문/인터뷰·관찰/비교·안전한 실험·개선안을 섞는다. 이유는 필요한 근거와 분석기준을 한 문장으로 쓴다. 원리형은 설문으로 증명하지 않는다."""
    try:
        parsed = _recommendation_rows(
            _compact_json_data("recommend", prompt, AI_TOKEN_BUDGETS["recommend"])
        )
        items = _normalize_recommendation_scores(parsed)
        if len(items) < 5:
            raise ValueError("AI response has too few recommendations")
        combined = items[:5]
        seen = {item["topic"] for item in combined}
        for offline_item in recommend_topics(tag, detail):
            if offline_item["topic"] not in seen:
                combined.append(offline_item)
                seen.add(offline_item["topic"])
            if len(combined) >= 10:
                break
        return {"mode": "online", "items": combined}
    except Exception as exc:
        return {"mode": "offline", "items": recommend_topics(tag, detail),
                "ai_error": "AI 추천을 생성하지 못해 오프라인 추천으로 전환했습니다.",
                "ai_error_code": type(exc).__name__}


def plan(topic: str):
    prompt = f"""주제: {topic}
짧은 Markdown 계획서: 핵심어2·범위·방법, 동기, 질문1+세부3, 대상/기간, 근거-수집-분석, 3주 일정, 윤리/한계, 산출물. 주제를 일반화하지 않는다."""
    try:
        return _compact_call("plan", prompt, AI_TOKEN_BUDGETS["plan"])
    except Exception:
        return make_plan(topic)


def guide(topic: str):
    prompt = f"""주제: {topic}
JSON 문자열 7개만. '단계—행동—산출물'. 순서=핵심어2/범위, 검색어4, 공신력 출처3종, 신뢰도, 근거 추출, 표·그래프, 결론·한계. 출처 양식=기관/제목/날짜/URL."""
    try:
        return _compact_json_list("guide", prompt, 7, AI_TOKEN_BUDGETS["guide"])
    except Exception:
        return make_research_guide(topic)


def survey(topic: str):
    prompt = f"""주제: {topic}
JSON 문자열 7개만. 익명안내, 대상조건, 행동/경험2, 원인/영향2, 서술1. 응답형식 포함, 한 문항 한 내용, 개인정보 금지. 원리 주제는 이해도만 측정."""
    try:
        return _compact_json_list("survey", prompt, 7, AI_TOKEN_BUDGETS["survey"])
    except Exception:
        return make_survey(topic)


def interview(topic: str):
    prompt = f"""주제: {topic}
JSON 문자열 7개만. 동의안내→경험→과정/원인→근거→자료와 차이→예외→제안/익명 분석. 열린 질문과 짧은 꼬리 질문 포함."""
    try:
        return _compact_json_list("interview", prompt, 7, AI_TOKEN_BUDGETS["interview"])
    except Exception:
        return make_interview(topic)


def report(topic: str, plan_text: str, log: str):
    plan_input = _compact_context(plan_text, 600)
    log_input = _compact_context(log, 1000)
    prompt = f"""주제: {topic}
계획:
{plan_input or '[없음]'}
학생이 실제로 기록한 내용:
{log_input or '[없음]'}

위 내용만으로 Markdown 보고서 초안을 작성하라. 없는 수치·출처·발언은 만들지 말고 ___[입력 안내]로 둔다.
목차: 주제 핵심, 동기·목적, 개념·출처, 대상·방법, 결과, 질문-근거-분석 표, 논의·다른 설명, 결론, 한계·후속 탐구, 학교 적용, 제출 확인표.
제목의 핵심어가 질문·자료·분석·결론에 이어지게 하고 근거가 없으면 [추가 조사 필요]로 표시한다."""
    try:
        return _compact_call("report", prompt, AI_TOKEN_BUDGETS["report"])
    except Exception:
        return make_report(topic, plan_text, log)


def get_runtime_cache_stats() -> dict:
    return {"entries": len(_RESULT_CACHE), "limit": _RESULT_CACHE_LIMIT}
