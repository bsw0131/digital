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
        "model": settings.get("model") or "gpt-4o-mini",
    }


def has_api_key() -> bool:
    config = get_online_config()
    return bool(config["enabled"] and config["api_key"])


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
        from openai import OpenAI

        client = OpenAI(api_key=config["api_key"])
        prompt = f"""
중학교 2학년 학생용 탐구활동 주제 20개를 추천하라.
관심 태그: {tag}
세부 관심사: {detail}

중요한 조건:
- 관심 태그가 2개이면 두 단어를 단순히 '+'로 붙인 제목을 만들지 말라.
- 두 관심사가 실제로 만나는 생활 장면, 학교 문제, 기술 활용, 행동 변화, 윤리 쟁점, 데이터 분석 가능성을 깊이 고민해 융합형 탐구 문제로 바꾸라.
- 예: '스포츠 + 로봇'이면 '스포츠 + 로봇에 대한 인식'이 아니라 로봇 보조 훈련, 경기 판정, 자세 교정, 부상 예방, 센서 데이터 분석처럼 두 분야가 실제로 연결되는 주제를 만들라.
- 학생이 학교에서 설문, 인터뷰, 자료조사, 간단한 관찰이나 실험으로 수행할 수 있어야 한다.
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
        return {"mode": "online", "items": items[:20]}
    except Exception:
        return {"mode": "offline", "items": recommend_topics(tag, detail)}


def plan(topic: str):
    return make_plan(topic)


def survey(topic: str):
    return make_survey(topic)


def guide(topic: str):
    return make_research_guide(topic)


def interview(topic: str):
    return make_interview(topic)


def report(topic: str, plan_text: str, log: str):
    return make_report(topic, plan_text, log)
