TEMPLATES = [
    ("{interest}에 대한 중학생의 인식과 선호도 분석", "사회", "하", "설문형", 3),
    ("{interest} 이용 시간이 학습 습관에 미치는 영향", "도덕", "중", "설문형", 3),
    ("{interest} 관련 데이터를 활용한 통계 분석", "수학", "중", "분석형", 4),
    ("{interest} 콘텐츠의 표현 방식과 설득 전략 분석", "국어", "중", "자료조사형", 3),
    ("{interest}와 관련된 과학적 원리 탐구", "과학", "상", "실험형", 5),
    ("{interest}가 친구 관계와 의사소통에 미치는 영향", "도덕", "중", "설문형", 3),
    ("{interest} 관련 직업과 미래 진로 탐색", "진로", "하", "자료조사형", 2),
    ("{interest} 문제를 해결하기 위한 학교 캠페인 설계", "사회", "중", "실천형", 4),
    ("{interest}와 청소년 소비 행동의 관계 탐구", "사회", "중", "설문형", 3),
    ("{interest} 관련 윤리적 쟁점 탐구", "도덕", "상", "자료조사형", 4),
]


def fit_scores(topic: str, inquiry_type: str = "") -> dict:
    data = 78
    survey = 55
    experiment = 45
    school = 70
    if inquiry_type == "설문형":
        survey += 30
        school += 10
    elif inquiry_type == "자료조사형":
        data += 18
    elif inquiry_type == "분석형":
        data += 12
        survey += 8
    elif inquiry_type == "실천형":
        school += 18
    elif inquiry_type == "실험형":
        experiment += 25
    vals = [max(5, min(100, x)) for x in [data, survey, experiment, school]]
    total = round(vals[0] * 0.30 + vals[1] * 0.25 + vals[2] * 0.20 + vals[3] * 0.25)
    return {
        "data_collection": vals[0],
        "survey": vals[1],
        "experiment": vals[2],
        "school_application": vals[3],
        "total": total,
    }


def recommend_topics(tag: str, detail: str) -> list[dict]:
    interest = detail.strip() or tag.strip() or "학교생활"
    items = []
    for template, subject, difficulty, inquiry_type, weeks in TEMPLATES:
        topic = template.format(interest=interest)
        fit = fit_scores(topic, inquiry_type)
        items.append({
            "topic": topic,
            "subject": subject,
            "difficulty": difficulty,
            "inquiry_type": inquiry_type,
            "duration": f"{weeks}주",
            "reason": f"'{interest}'라는 관심사를 학교에서 조사 가능한 탐구 문제로 바꾼 주제입니다.",
            "fit": fit,
        })
    items.sort(key=lambda x: x["fit"]["total"], reverse=True)
    return items


def make_plan(topic: str) -> str:
    return f"""탐구 주제: {topic}

1. 탐구 동기
이 주제가 나와 친구들의 생활과 어떤 관련이 있는지 궁금해서 탐구한다.

2. 탐구 문제
{topic}에 대해 학생들은 어떤 생각을 가지고 있으며, 학교생활에 어떤 영향을 줄까?

3. 탐구 방법
- 관련 자료를 조사한다.
- 친구들을 대상으로 설문을 실시한다.
- 결과를 표와 그래프로 정리한다.
- 분석 결과를 바탕으로 개선 방안을 제안한다.

4. 예상 결과
학생들의 인식과 행동 특성을 파악하고, 학교에서 실천할 수 있는 제안을 만들 수 있다.
"""


def make_survey(topic: str) -> list[str]:
    return [
        f"{topic}에 대해 얼마나 관심이 있나요?",
        f"{topic}이 학교생활에 영향을 준다고 생각하나요?",
        f"{topic}과 관련해 가장 중요하다고 생각하는 점은 무엇인가요?",
        "이 주제를 더 잘 이해하기 위해 학교에서 할 수 있는 활동은 무엇인가요?",
        "자유롭게 의견을 적어 주세요.",
    ]


def make_research_guide(topic: str) -> list[str]:
    return [
        "학교도서관, 뉴스, 공공기관 자료처럼 출처가 분명한 자료를 찾는다.",
        "자료의 작성자, 날짜, 기관을 기록한다.",
        "설문 결과는 표와 그래프로 정리한다.",
        "찾은 자료와 설문 결과가 탐구 문제에 답하는지 확인한다.",
    ]


def make_interview(topic: str) -> list[str]:
    return [
        f"{topic}에 대해 어떤 경험이 있나요?",
        "이 문제를 해결하거나 개선하려면 무엇이 필요하다고 생각하나요?",
        "친구들에게 조언하고 싶은 점이 있나요?",
    ]


def make_report(topic: str, plan_text: str, log: str) -> str:
    return f"""# 탐구 보고서 초안

## 1. 탐구 주제
{topic}

## 2. 탐구 계획
{plan_text}

## 3. 탐구 과정
{log or '탐구 과정과 조사 내용을 여기에 정리하세요.'}

## 4. 결과 분석
설문과 자료조사 결과를 바탕으로 핵심 경향을 정리하세요.

## 5. 결론 및 제안
탐구를 통해 알게 된 점과 학교에서 실천할 수 있는 제안을 작성하세요.
"""
