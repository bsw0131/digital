INTEREST_PROFILES = {
    "게임": ("게임 활동", "몰입, 전략 선택, 협동 경험"),
    "스포츠": ("운동 경기와 훈련", "기록 향상, 자세 교정, 부상 예방"),
    "음악": ("음악 감상과 창작", "감정 변화, 집중, 표현 방식"),
    "K-POP": ("K-POP 팬 활동과 콘텐츠", "문화 확산, 팬덤 소통, 미디어 영향"),
    "유튜브": ("영상 플랫폼 이용", "추천 알고리즘, 시청 습관, 정보 신뢰도"),
    "웹툰": ("웹툰 콘텐츠", "서사 구조, 그림 표현, 독자 반응"),
    "영화": ("영화 감상과 장면 연출", "메시지 전달, 감정 변화, 사회 문제 표현"),
    "음식": ("음식 선택과 식생활", "건강, 소비 습관, 문화 차이"),
    "동물": ("동물 행동과 공존", "생명 존중, 돌봄, 환경 적응"),
    "환경": ("환경 보호 실천", "자원 절약, 탄소 배출, 생활 속 변화"),
    "패션": ("패션과 자기표현", "소비 선택, 유행, 개성 표현"),
    "친구관계": ("친구 관계와 소통", "공감, 갈등 해결, 협력"),
    "스마트폰": ("스마트폰 사용", "생활 습관, 집중력, 디지털 안전"),
    "진로": ("진로 탐색", "직업 이해, 역량 준비, 미래 변화"),
    "과학": ("과학 원리와 실험", "관찰, 변인 통제, 원리 적용"),
    "로봇": ("로봇 기술과 자동화", "센서 활용, 반복 작업, 인간 보조"),
    "AI": ("인공지능 활용", "추천, 예측, 판단 보조, 윤리"),
    "건강": ("건강한 생활 습관", "운동, 수면, 스트레스 관리"),
    "여행": ("여행 경험과 지역 탐색", "문화 이해, 이동, 지역 문제"),
    "학교생활": ("학교생활", "학습, 관계, 규칙, 공간 활용"),
}

FUSION_TEMPLATES = [
    ("{context}에서 {b_domain}을 활용하면 {a_focus}에 어떤 변화가 생길까?", "과학", "중", "설문형", 3),
    ("{context}을 개선하기 위한 {b_domain} 활용 아이디어 설계", "정보", "중", "실천형", 4),
    ("{a_domain} 문제를 해결하는 {b_domain} 사례 조사와 학교 적용 가능성", "사회", "중", "자료조사형", 3),
    ("{context}에 대한 학생들의 기대와 걱정 비교", "도덕", "중", "설문형", 3),
    ("{b_domain}이 {a_domain}의 참여도와 흥미에 미치는 영향", "사회", "중", "설문형", 3),
    ("{context} 관련 데이터를 수집해 효과를 분석하기", "수학", "상", "분석형", 4),
    ("{a_domain}에서 {b_domain}을 안전하게 활용하기 위한 기준 만들기", "도덕", "중", "자료조사형", 3),
    ("{context}을 주제로 한 학교 캠페인 또는 안내자료 제작", "국어", "하", "실천형", 3),
    ("{b_domain} 활용 전후의 {a_focus} 변화를 비교하는 탐구", "과학", "상", "실험형", 5),
    ("{context}에 대한 친구들의 경험을 인터뷰로 분석하기", "국어", "중", "인터뷰형", 3),
    ("{a_domain} 속 불편함을 {b_domain}으로 해결하는 생활 발명 아이디어", "기술", "중", "실천형", 4),
    ("{context} 관련 뉴스와 영상의 관점 차이 비교", "국어", "중", "자료조사형", 3),
    ("{b_domain}이 {a_domain}의 공정성과 신뢰도에 미치는 영향", "사회", "상", "자료조사형", 4),
    ("{context}에 필요한 학생용 체크리스트 만들기", "진로", "하", "실천형", 2),
    ("{a_domain}을 더 재미있게 만드는 {b_domain} 요소 분석", "정보", "중", "분석형", 4),
    ("{context}에서 발생할 수 있는 윤리적 쟁점 탐구", "도덕", "상", "자료조사형", 4),
    ("{b_domain}을 활용한 {a_domain} 학습 도구의 장단점 분석", "정보", "중", "설문형", 3),
    ("{context}을 학교 동아리 활동으로 운영하는 방법 제안", "진로", "하", "실천형", 3),
    ("{a_domain} 경험이 많은 학생과 적은 학생의 {b_domain} 인식 비교", "사회", "중", "설문형", 3),
    ("{context}을 주제로 한 작은 실험 또는 관찰 계획 세우기", "과학", "중", "실험형", 4),
]

SINGLE_TEMPLATES = [
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
    ("{interest}가 학교생활 만족도에 미치는 영향", "사회", "중", "설문형", 3),
    ("{interest}를 주제로 한 학급 토론 자료 만들기", "국어", "하", "자료조사형", 2),
    ("{interest} 경험 차이에 따른 학생 의견 비교", "사회", "중", "설문형", 3),
    ("{interest}와 미디어 사용 습관의 관계 탐구", "정보", "중", "분석형", 4),
    ("{interest}를 활용한 학교 문제 해결 아이디어 제안", "사회", "중", "실천형", 4),
    ("{interest} 관련 뉴스의 관점과 신뢰도 비교", "국어", "상", "자료조사형", 4),
    ("{interest}가 청소년 건강과 생활 리듬에 미치는 영향", "보건", "중", "설문형", 3),
    ("{interest}와 환경 보호 실천 방법 연결하기", "과학", "중", "실천형", 4),
    ("{interest}에 숨어 있는 수학적 패턴 찾기", "수학", "상", "분석형", 4),
    ("{interest}를 더 안전하고 올바르게 이용하는 방법 탐구", "도덕", "중", "자료조사형", 3),
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
    elif inquiry_type == "인터뷰형":
        survey += 15
        data += 8
    vals = [max(5, min(100, x)) for x in [data, survey, experiment, school]]
    total = round(vals[0] * 0.30 + vals[1] * 0.25 + vals[2] * 0.20 + vals[3] * 0.25)
    return {
        "data_collection": vals[0],
        "survey": vals[1],
        "experiment": vals[2],
        "school_application": vals[3],
        "total": total,
    }


def _split_tags(tag: str) -> list[str]:
    return [part.strip() for part in tag.split("+") if part.strip()]


def _profile(name: str) -> tuple[str, str]:
    return INTEREST_PROFILES.get(name, (name, "학생들의 생각, 생활 변화, 학교 적용 가능성"))


def _fusion_context(tags: list[str], detail: str) -> dict:
    first = tags[0] if tags else detail
    second = tags[1] if len(tags) > 1 else detail
    a_domain, a_focus = _profile(first)
    b_domain, b_focus = _profile(second)
    if detail and tags:
        context = f"{detail} 상황에서 {a_domain}과 {b_domain}이 만나는 지점"
    else:
        context = f"{a_domain}과 {b_domain}이 만나는 생활 속 장면"
    return {
        "a_domain": a_domain,
        "a_focus": a_focus,
        "b_domain": b_domain,
        "b_focus": b_focus,
        "context": context,
    }


def recommend_topics(tag: str, detail: str) -> list[dict]:
    tags = _split_tags(tag.strip())
    detail = detail.strip()
    is_fusion = len(tags) >= 2 or (len(tags) == 1 and detail)

    items = []
    if is_fusion:
        context = _fusion_context(tags, detail)
        for template, subject, difficulty, inquiry_type, weeks in FUSION_TEMPLATES:
            topic = template.format(**context)
            fit = fit_scores(topic, inquiry_type)
            items.append({
                "topic": topic,
                "subject": subject,
                "difficulty": difficulty,
                "inquiry_type": inquiry_type,
                "duration": f"{weeks}주",
                "reason": f"선택한 관심사를 단순히 나열하지 않고, '{context['context']}'에서 조사할 수 있는 문제로 바꾼 주제입니다.",
                "fit": fit,
            })
    else:
        interest = detail or (tags[0] if tags else "학교생활")
        for template, subject, difficulty, inquiry_type, weeks in SINGLE_TEMPLATES:
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
    return items[:20]


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
