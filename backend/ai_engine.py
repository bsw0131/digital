import json
import os

from dotenv import load_dotenv

from offline_engine import (
    make_interview,
    make_plan,
    make_report,
    make_research_guide,
    make_survey,
    recommend_topics,
)

load_dotenv()


def has_api_key() -> bool:
    return bool(os.getenv("OPENAI_API_KEY"))


def recommend(tag: str, detail: str):
    if not has_api_key():
        return {"mode": "offline", "items": recommend_topics(tag, detail)}

    try:
        from openai import OpenAI

        client = OpenAI()
        prompt = f"""
중학교 2학년 학생용 탐구활동 주제 20개를 추천하라.
관심 태그: {tag}
세부 관심사: {detail}
관심 태그가 2개이면 두 관심사가 연결된 융합형 탐구 주제를 우선 추천하라.
각 항목은 topic, subject, difficulty, inquiry_type, duration, reason, fit(data_collection, survey, experiment, school_application, total)를 가진 JSON 배열로만 출력하라.
fit.total 점수가 높은 순서로 정렬하라.
"""
        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        text = res.choices[0].message.content.strip().replace("```json", "").replace("```", "")
        items = json.loads(text)
        items.sort(key=lambda x: (x.get("fit") or {}).get("total", 0), reverse=True)
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
