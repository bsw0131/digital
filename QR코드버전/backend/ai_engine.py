import json

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
from settings_store import get_ai_settings_private

load_dotenv()


def get_online_config() -> dict:
    settings = get_ai_settings_private()
    return {
        "enabled": bool(settings.get("online_ai_enabled")),
        "api_key": settings.get("openai_api_key", ""),
        "model": settings.get("model") or "gpt-5.6-terra",
    }


def has_api_key() -> bool:
    config = get_online_config()
    return bool(config["enabled"] and config["api_key"])


def _online_client(config: dict):
    from openai import OpenAI

    return OpenAI(api_key=config["api_key"])


def _clean_json_text(text: str) -> str:
    return (text or "").strip().replace("```json", "").replace("```", "").strip()


def _online_text(system: str, prompt: str, temperature: float = 0.65) -> str:
    config = get_online_config()
    if not (config["enabled"] and config["api_key"]):
        raise RuntimeError("online ai disabled")
    client = _online_client(config)
    res = client.chat.completions.create(
        model=config["model"],
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
    )
    return (res.choices[0].message.content or "").strip()


def _online_json_list(system: str, prompt: str, min_items: int = 4, max_items: int = 7) -> list[str]:
    text = _online_text(system, prompt, 0.7)
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
너는 중·고등학생 탐구활동을 돕는 한국어 AI 튜터다.
오프라인 템플릿보다 더 구체적이고 주제 맞춤형이어야 한다.
학생이 실제 학교에서 자료조사, 설문, 인터뷰, 관찰, 간단한 실험으로 수행할 수 있게 안내한다.
막연한 표현, 반복 문장, '조사해 보세요'식 일반론을 피하고 조사 대상, 자료 출처, 비교 기준, 분석 방법을 구체화한다.
과장된 결론이나 검증 불가능한 활동은 제안하지 않는다.
"""


def _weeks_from_duration(value) -> int:
    digits = "".join(ch for ch in str(value or "") if ch.isdigit())
    return int(digits) if digits else 3


def _normalize_recommendation_scores(items: list[dict]) -> list[dict]:
    normalized = []
    for item in items:
        topic = item.get("topic") or ""
        if not topic:
            continue
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
중·고등학생용 탐구활동 주제를 반드시 15개 추천하라.
관심 태그: {tag}
세부 관심사: {detail}

중요한 조건:
- 관심 태그 또는 세부 관심사가 2개이면 두 단어를 단순히 '+'로 붙인 제목을 만들지 말라.
- 두 관심사가 자연스럽게 연결되지 않으면 억지로 융합하지 말고, 각 관심사에서 좋은 탐구주제를 균형 있게 섞어 추천하라.
- 직접 입력이 '축구,농구'처럼 같은 분야의 두 관심사여도 단순 나열하지 말고 선택 기준, 참여 동기, 안전, 학교 적용, 친구 관계, 건강 습관처럼 연구 가능한 관계로 바꾸라.
- 두 관심사가 실제로 만나는 생활 장면, 학교 문제, 기술 활용, 행동 변화, 윤리 쟁점, 데이터 분석 가능성을 깊이 고민해 융합형 탐구 문제로 바꾸라.
- 예: '스포츠 + 로봇'이면 '스포츠 + 로봇에 대한 인식'이 아니라 로봇 보조 훈련, 경기 판정, 자세 교정, 부상 예방, 센서 데이터 분석처럼 두 분야가 실제로 연결되는 주제를 만들라.
- 예: '여행 + 음식'이면 '여행·음식이 만나는 생활 장면' 같은 추상 제목보다 지역 음식이 여행 만족도에 미치는 영향, SNS 맛집 정보가 여행 계획에 주는 영향, 여행지 식비 계획과 만족도, 지역 음식과 문화 이해처럼 실제 조사 장면이 보이는 제목을 만들라.
- 수학·과학뿐 아니라 게임, 음악, 웹툰, 스포츠, 패션, 음식, 친구관계, 진로, 학교생활 등 모든 분야에서 자료 분석, 변인 비교, 윤리 판단, 개선 설계, 진로·사회적 의미가 드러나는 전문적인 주제를 섞어 추천하라.
- 사용자가 원주율, 방정식, 혈액, 전류처럼 개념을 입력하면 '원주율을 활용한 데이터 분석'처럼 넓게 쓰지 말고 '원주율은 왜 3.14로 시작할까?', '원주율이 무리수인 이유는 무엇일까?', '방정식에서 미지수는 왜 필요한가?', '혈액은 왜 산소 운반에 적합한 구조를 가질까?'처럼 개념의 정의, 원리, 증명, 구조, 조건을 파고드는 질문형 제목을 우선하라.
- 학생이 학교에서 설문, 인터뷰, 자료조사, 간단한 관찰이나 실험으로 수행할 수 있어야 한다.
- '인식 조사'처럼 넓은 제목보다 원인, 영향, 비교 기준, 해결 방법이 드러나는 구체적 제목을 우선하라.
- 제목에는 가능하면 '+' 기호를 쓰지 말라.

각 항목은 topic, subject, difficulty, inquiry_type, duration, reason, fit(data_collection, survey, experiment, school_application, total)를 가진 JSON 배열로만 출력하라.
fit.total 점수가 높은 순서로 정렬하라.
"""
        res = client.chat.completions.create(
            model=config["model"],
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        text = res.choices[0].message.content.strip().replace("```json", "").replace("```", "")
        items = _normalize_recommendation_scores(json.loads(text))
        return {"mode": "online", "items": items[:15]}
    except Exception:
        return {"mode": "offline", "items": recommend_topics(tag, detail)}


def plan(topic: str):
    try:
        return _online_text(
            QUALITY_RULES,
            f"""
탐구 주제: {topic}

이 주제로 바로 시작할 수 있는 탐구계획서를 작성하라.
반드시 아래 형식을 지켜라.

1. 탐구 동기: 학생 생활과 연결해 3~4문장
2. 탐구 문제: 핵심 질문 1개와 세부 질문 3개
3. 탐구 대상과 범위: 조사 대상, 표본 수, 기간, 장소
4. 탐구 방법:
   - 자료조사: 찾아볼 자료 출처와 확인할 기준
   - 설문: 응답 대상과 주요 문항 방향
   - 인터뷰/관찰: 누구에게 무엇을 물을지 또는 무엇을 볼지
5. 분석 계획: 표, 그래프, 비교 기준, 예상되는 한계
6. 예상 결과와 활용: 학교에서 적용 가능한 제안

중학생도 이해할 수 있게 쓰되, 내용은 구체적이고 전문적으로 만들어라.
""",
            0.62,
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

이 주제에 맞는 학생 설문 문항을 7개 만들어라.
조건:
- JSON 배열만 출력한다.
- 객관식, 5점 척도, 단답형, 이유 서술형을 섞는다.
- 각 문항에는 응답자가 무엇을 기준으로 답해야 하는지 드러나야 한다.
- 개인정보를 묻지 말고, 학교에서 실제로 조사 가능한 문항으로 만든다.
- 주제의 원인, 영향, 비교 기준, 실천 가능성을 모두 확인할 수 있게 한다.
""",
            min_items=5,
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

이 주제에 맞는 자료조사 가이드를 6개 단계로 만들어라.
조건:
- JSON 배열만 출력한다.
- 각 단계는 학생이 실제로 할 행동으로 시작한다.
- 자료 출처 예시, 확인할 기준, 기록 방법, 신뢰도 점검, 설문/인터뷰와 연결할 방법을 포함한다.
- 주제가 환경, 기술, 건강, 미디어, 스포츠, 소비, 학교생활 등 무엇인지에 맞춰 자료 종류를 다르게 제안한다.
- 단순히 '인터넷에서 찾아본다'라고 쓰지 말고 구체적인 자료와 비교 기준을 제시한다.
""",
            min_items=5,
            max_items=6,
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

이 주제에 맞는 인터뷰 질문과 진행 방법을 6개 만들어라.
조건:
- JSON 배열만 출력한다.
- 첫 항목에는 인터뷰 대상 추천을 포함한다.
- 질문은 경험, 이유, 구체적 사례, 자료조사와 다른 점, 개선 제안이 드러나야 한다.
- 예/아니오로 끝나는 질문을 피하고, 후속 질문이 가능하게 만든다.
- 학생이 학교 안에서 안전하게 진행할 수 있는 방식으로 작성한다.
""",
            min_items=5,
            max_items=6,
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

학생이 작성한 탐구계획서:
{plan_text or '아직 충분히 작성되지 않았습니다.'}

학생이 모은 메모와 탐구일지:
{log or '아직 충분히 작성되지 않았습니다.'}

위 내용을 바탕으로 보고서 초안을 작성하라.
조건:
- Markdown 형식으로 작성한다.
- 학생이 실제로 채워 넣어야 할 빈칸은 `___`로 표시한다.
- 자료조사, 설문, 인터뷰, 관찰 결과가 어떻게 연결되는지 설명한다.
- 근거가 부족한 부분은 단정하지 말고 '추가 확인 필요'라고 표시한다.
- 아래 목차를 포함한다:
  1. 탐구 주제
  2. 탐구 동기
  3. 탐구 문제
  4. 탐구 방법
  5. 조사 결과 정리
  6. 결과 분석
  7. 결론
  8. 학교 적용 제안
  9. 보완할 점
""",
            0.58,
        )
    except Exception:
        pass
    return make_report(topic, plan_text, log)
