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
from settings_store import DEFAULT_MODEL, get_ai_settings_private, refresh_ai_model

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

    return OpenAI(api_key=api_key, timeout=35.0, max_retries=1)


def _online_client(config: dict):
    return _cached_online_client(config["api_key"])


def _clean_json_text(text: str) -> str:
    return (text or "").strip().replace("＇＇＇json", "").replace("＇＇＇", "").replace("```json", "").replace("```", "").strip()


def _chat_completion(config: dict, messages: list[dict], max_tokens: int):
    from openai import BadRequestError, OpenAIError

    client = _online_client(config)

    def create(model: str):
        params = {"model": model, "messages": messages}
        try:
            return client.chat.completions.create(**params, max_completion_tokens=max_tokens)
        except BadRequestError as exc:
            message = str(exc).lower()
            if "max_completion_tokens" not in message and "unsupported parameter" not in message:
                raise
            return client.chat.completions.create(**params, max_tokens=max_tokens)

    try:
        return create(config["model"])
    except OpenAIError:
        new_model = refresh_ai_model(config["api_key"], config.get("model", ""))
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
- reason에는 추천 이유뿐 아니라 '수집할 자료/대상, 핵심 비교 기준, 가능한 분석법'을 2~3문장으로 구체적으로 적는다.
- difficulty는 중/중상/상 중 하나, duration은 2주/3주/4주 중 하나로 쓴다.
- fit은 0~100 정수로 작성하되 실제 점수는 서버에서 다시 계산한다.

반드시 아래 키를 가진 JSON 배열만 출력한다. 설명이나 코드블록은 붙이지 않는다.
[
  {
    "topic": "구체적인 탐구 질문 또는 제목",
    "subject": "관련 교과 1~2개",
    "difficulty": "중|중상|상",
    "inquiry_type": "주된 탐구 방법",
    "duration": "2주|3주|4주",
    "reason": "수행 방법과 분석 기준까지 포함한 구체적 설명",
    "fit": {
      "data_collection": 0,
      "survey": 0,
      "experiment": 0,
      "school_application": 0,
      "total": 0
    }
  }
]
"""
        res = _chat_completion(config, [{"role": "user", "content": prompt}], 4200)
        text = _clean_json_text(res.choices[0].message.content)
        items = _normalize_recommendation_scores(json.loads(text))
        if len(items) < 10:
            raise ValueError("AI response has too few recommendations")
        return {"mode": "online", "items": items[:15]}
    except Exception as exc:
        return {
            "mode": "offline",
            "items": recommend_topics(tag, detail),
            "ai_error": f"OpenAI 생성 요청 실패 ({type(exc).__name__})",
        }


def plan(topic: str):
    try:
        return _online_text(
            QUALITY_RULES,
            f"""
탐구 주제: {topic}

이 주제로 학생이 그대로 실행할 수 있는 탐구계획서를 작성하라. 각 항목은 주제에 맞춘 실제 내용으로 채우고 다음 구조를 지킨다.

1. 탐구 동기
- 학생 생활 또는 사회·교과 맥락과 연결한 3~4문장
- 왜 이 주제를 확인할 가치가 있는지 설명

2. 탐구 문제
- 답을 미리 정하지 않은 핵심 질문 1개
- 핵심 질문을 검증하는 세부 질문 3개
- 비교할 독립 변인과 관찰할 종속 변인(해당되는 경우)을 쉬운 말로 표시

3. 예상과 근거
- 예상 결과 1~2개와 그렇게 예상하는 이유
- 예상은 가설이며 실제 결과가 아님을 명시

4. 탐구 대상과 범위
- 조사·관찰 대상, 권장 표본 수, 비교 집단, 기간, 장소, 제외 범위
- 표본을 구하기 어려울 때 가능한 대안

5. 자료 수집 계획
- 신뢰할 만한 자료 출처 유형 3개와 검색어 예시
- 설문·인터뷰·관찰·간이 실험 중 적합한 방법, 횟수와 기록 양식
- 개인정보 보호, 동의, 안전 주의점

6. 분석 계획
- 표 또는 그래프 종류와 축에 넣을 값
- 평균, 비율, 빈도, 조건별 비교 중 사용할 방법
- 어떤 결과가 나오면 핵심 질문을 어떻게 해석할지 판단 기준

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

조건:
- JSON 문자열 배열만 출력한다.
- 각 항목은 '단계명 — 할 일 — 기록할 내용/산출물' 형식의 구체적인 실행 문장으로 쓴다.
- 반드시 다음을 포함한다: 핵심 개념과 검색어 만들기, 공신력 있는 출처 찾기, 출처 신뢰도 확인, 서로 다른 자료 교차 검증, 필요한 수치·사례 추출, 표로 비교 정리, 설문·인터뷰 결과와 연결하기.
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

조건:
- JSON 문자열 배열만 출력한다.
- 첫 항목은 적합한 인터뷰 대상 2~3유형, 선정 이유, 요청 방법, 예상 시간, 녹음·익명 처리 동의 안내를 포함한다.
- 질문은 쉬운 시작 질문 → 구체적 경험 → 원인과 판단 기준 → 자료조사와 다른 점 → 문제점 → 개선 제안 순서로 깊어지게 한다.
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
- 계획서의 탐구 문제와 실제 수집 자료, 분석, 결론이 일관되게 이어지는지 확인한다.
- 결과와 해석을 분리하고, 상관관계를 인과관계로 단정하지 않는다.
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
