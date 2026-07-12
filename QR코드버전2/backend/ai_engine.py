import json
from settings_store import get_ai_settings_private

BASE_TOPICS = [
    ("{a}와 {b}이 만나는 학교생활 문제 탐구", "사회", "설문형", 3),
    ("{a} 경험이 {b} 인식에 미치는 영향", "도덕", "설문형", 3),
    ("{a}와 {b} 관련 데이터를 수집해 경향 분석하기", "수학", "분석형", 4),
    ("{a}와 {b}를 활용한 학교 캠페인 또는 안내자료 제작", "국어", "실천형", 3),
    ("{a}와 {b}의 장단점 비교와 개선 방안", "사회", "자료조사형", 3),
    ("{a}와 {b}에 대한 중학생의 기대와 걱정 비교", "도덕", "설문형", 3),
    ("{a}와 {b}를 안전하게 활용하기 위한 기준 만들기", "정보", "자료조사형", 3),
    ("{a}와 {b} 관련 친구들의 경험 인터뷰 분석", "국어", "인터뷰형", 3),
    ("{a}와 {b}를 연결한 생활 속 문제 해결 아이디어", "기술", "실천형", 4),
    ("{a}와 {b} 관련 뉴스와 영상의 관점 차이 비교", "국어", "자료조사형", 3),
    ("{a}가 학습 습관과 학교생활에 미치는 영향", "사회", "설문형", 3),
    ("{a} 관련 자료를 활용한 통계 분석", "수학", "분석형", 4),
    ("{a}에 대한 중학생의 선호도와 인식 조사", "사회", "설문형", 3),
    ("{a}와 관련된 직업과 미래 진로 탐색", "진로", "자료조사형", 2),
    ("{a}를 더 올바르게 이용하는 방법 탐구", "도덕", "자료조사형", 3),
    ("{a} 관련 학교 문제 해결 제안", "사회", "실천형", 4),
    ("{a} 콘텐츠의 표현 방식과 설득 전략 분석", "국어", "자료조사형", 3),
    ("{a}와 청소년 건강 또는 생활 리듬의 관계", "보건", "설문형", 3),
    ("{a}와 환경 보호 실천 방법 연결하기", "과학", "실천형", 4),
    ("{a} 경험 차이에 따른 학생 의견 비교", "사회", "설문형", 3),
]


def _parts(tag, detail):
    items = [x.strip() for x in (tag or "").replace("+", ",").split(",") if x.strip()]
    items += [x.strip() for x in (detail or "").replace("+", ",").split(",") if x.strip()]
    if not items:
        items = ["학교생활"]
    return items[:2]


def _fit(topic, inquiry_type, weeks):
    base = 72
    if inquiry_type == "설문형": base += 8
    if inquiry_type == "실천형": base += 6
    if inquiry_type == "분석형": base += 5
    base += min(8, len(topic) % 9)
    return {
        "data_collection": min(98, base + 4),
        "survey": min(98, base + (10 if inquiry_type == "설문형" else 0)),
        "experiment": max(35, base - 18 + weeks),
        "school_application": min(98, base + (8 if inquiry_type == "실천형" else 2)),
        "total": min(98, base + 4),
    }


def offline_recommend(tag, detail):
    parts = _parts(tag, detail)
    a = parts[0]
    b = parts[1] if len(parts) > 1 else "학교생활"
    items = []
    for template, subject, inquiry_type, weeks in BASE_TOPICS:
        topic = template.format(a=a, b=b)
        fit = _fit(topic, inquiry_type, weeks)
        items.append({
            "topic": topic,
            "subject": subject,
            "difficulty": "중",
            "inquiry_type": inquiry_type,
            "duration": f"{weeks}주",
            "reason": "학생 관심사를 학교에서 조사 가능한 탐구 문제로 바꾼 주제입니다.",
            "fit": fit,
        })
    items.sort(key=lambda x: x["fit"]["total"], reverse=True)
    return items[:20]


def recommend(tag, detail):
    config = get_ai_settings_private()
    if not (config["online_ai_enabled"] and config["openai_api_key"]):
        return {"mode": "offline", "items": offline_recommend(tag, detail)}
    try:
        from openai import OpenAI
        client = OpenAI(api_key=config["openai_api_key"])
        prompt = f"중학교 탐구 주제 20개를 JSON 배열로 추천해줘. 관심 태그: {tag}, 세부 관심사: {detail}. 각 항목은 topic, subject, difficulty, inquiry_type, duration, reason, fit를 포함해."
        res = client.chat.completions.create(model=config["model"], messages=[{"role": "user", "content": prompt}], temperature=0.7)
        text = res.choices[0].message.content.strip().replace("```json", "").replace("```", "")
        return {"mode": "online", "items": json.loads(text)[:20]}
    except Exception:
        return {"mode": "offline", "items": offline_recommend(tag, detail)}


def plan(topic):
    return f"""탐구 주제: {topic}

1. 탐구 동기
이 주제가 나와 친구들의 생활과 어떤 관련이 있는지 궁금해서 탐구한다.

2. 탐구 문제
{topic}에 대해 학생들은 어떤 생각을 가지고 있으며, 학교생활에 어떤 영향을 줄까?

3. 탐구 방법
- 관련 자료를 조사한다.
- 친구들을 대상으로 설문을 실시한다.
- 필요하면 인터뷰를 진행한다.
- 결과를 표와 그래프로 정리한다.

4. 예상 결과
학생들의 인식과 행동 특성을 파악하고 학교에서 실천할 수 있는 제안을 만들 수 있다.
"""


def guide(topic):
    return [
        f"'{topic}'와 관련된 공공기관 자료, 뉴스, 학교 사례를 찾아봅니다.",
        "자료마다 출처, 작성 날짜, 기관명을 기록합니다.",
        "원인, 영향, 해결 방법으로 자료를 나누어 정리합니다.",
        "설문이나 인터뷰로 확인할 수 있는 내용을 표시합니다.",
        "마지막에는 학교에서 실천 가능한 제안과 연결합니다.",
    ]


def survey(topic):
    return [
        f"'{topic}'와 관련된 경험이 있나요?",
        "이 주제가 학교생활에 영향을 준다고 생각하나요?",
        "가장 중요하게 생각하는 기준은 무엇인가요?",
        "문제가 있다면 가장 큰 원인은 무엇이라고 생각하나요?",
        "학교에서 실천할 수 있는 해결 방법은 무엇인가요?",
    ]


def interview(topic):
    return [
        f"'{topic}'와 관련해 직접 겪은 경험을 말해 주세요.",
        "그 경험에서 가장 중요하다고 느낀 점은 무엇인가요?",
        "이 주제를 더 잘 조사하려면 어떤 자료가 필요할까요?",
        "학교에서 실천 가능한 개선 방법은 무엇이라고 생각하나요?",
        "친구들에게 꼭 묻고 싶은 질문은 무엇인가요?",
    ]


def report(topic, plan_text, log):
    return f"""# 탐구 보고서 초안

## 1. 탐구 주제
{topic}

## 2. 탐구 동기
이 주제는 학생들의 생활과 학교 문제를 이해하는 데 도움이 된다고 생각했다.

## 3. 탐구 문제
{topic}에 대해 학생들은 어떤 경험과 생각을 가지고 있는가?

## 4. 탐구 방법
자료조사, 설문, 인터뷰, 탐구일지를 활용하여 근거를 모았다.

## 5. 탐구계획서 요약
{plan_text or '탐구계획서를 바탕으로 내용을 보완하세요.'}

## 6. 내가 정리한 내용
{log or '탐구일지와 메모를 더 작성한 뒤 보고서를 보완하세요.'}

## 7. 결론 및 제안
조사 결과를 바탕으로 학교에서 실천할 수 있는 개선 방안을 제안한다. 설문 결과와 자료 출처를 추가하면 보고서의 신뢰도가 높아진다.
"""
