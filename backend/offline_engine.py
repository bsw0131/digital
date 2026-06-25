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


QUESTION_PROFILES = [
    {
        "keywords": ["AI", "인공지능", "알고리즘", "추천", "로봇", "자동화", "센서"],
        "experience": "이 기술을 직접 사용하거나 본 경험",
        "factor": "정확성, 편리함, 개인정보 보호, 공정성",
        "comparison": "기술을 사용할 때와 사용하지 않을 때의 차이",
        "solution": "더 안전하고 유용하게 쓰기 위한 기준",
        "expert": "기술의 장점과 오류 가능성을 모두 설명할 수 있는 사람",
    },
    {
        "keywords": ["스포츠", "운동", "훈련", "경기", "자세", "부상", "기록"],
        "experience": "운동이나 경기에서 기록, 자세, 부상 예방을 신경 쓴 경험",
        "factor": "기록 향상, 안전, 흥미, 꾸준한 참여",
        "comparison": "훈련 방법이나 도구를 사용하기 전후의 차이",
        "solution": "학교에서 실천할 수 있는 훈련 또는 안전 수칙",
        "expert": "운동 경험이 많거나 체육 활동을 지도해 본 사람",
    },
    {
        "keywords": ["유튜브", "영상", "미디어", "스마트폰", "SNS", "콘텐츠", "웹툰", "영화", "K-POP"],
        "experience": "해당 콘텐츠나 플랫폼을 이용한 경험",
        "factor": "몰입도, 정보 신뢰도, 추천 방식, 생활 습관 변화",
        "comparison": "이용 시간이 많을 때와 적을 때의 차이",
        "solution": "건강하고 비판적으로 이용하기 위한 방법",
        "expert": "콘텐츠를 자주 이용하거나 미디어 사용 습관을 조절해 본 사람",
    },
    {
        "keywords": ["환경", "탄소", "재활용", "쓰레기", "에너지", "기후", "동물", "생태"],
        "experience": "생활 속 환경 문제를 보거나 해결하려고 해 본 경험",
        "factor": "실천 가능성, 비용, 효과, 지속 가능성",
        "comparison": "실천 전후 또는 장소별 환경 변화의 차이",
        "solution": "학교에서 바로 해 볼 수 있는 환경 실천 방안",
        "expert": "환경 활동에 참여했거나 학교 공간의 문제를 잘 아는 사람",
    },
    {
        "keywords": ["건강", "수면", "스트레스", "음식", "식생활", "급식", "보건"],
        "experience": "건강 습관이나 식생활을 바꾸려고 해 본 경험",
        "factor": "건강 영향, 실천 난이도, 만족도, 생활 리듬",
        "comparison": "습관이 좋을 때와 나쁠 때의 몸과 생활 차이",
        "solution": "중학생에게 현실적으로 맞는 건강 실천 방법",
        "expert": "건강 습관을 관리해 본 사람이나 관련 지식을 가진 사람",
    },
    {
        "keywords": ["친구", "관계", "소통", "학교생활", "학습", "수업", "진로", "직업"],
        "experience": "학교생활, 친구 관계, 학습, 진로와 관련해 겪은 경험",
        "factor": "만족도, 갈등 원인, 도움 정도, 학교 적용 가능성",
        "comparison": "경험이 많은 학생과 적은 학생의 생각 차이",
        "solution": "학급이나 학교에서 실천할 수 있는 개선 방법",
        "expert": "비슷한 경험을 했거나 친구들의 의견을 잘 들을 수 있는 사람",
    },
    {
        "keywords": ["패션", "소비", "쇼핑", "브랜드", "여행", "문화"],
        "experience": "선택, 소비, 문화 경험에서 영향을 받은 일",
        "factor": "가격, 유행, 자기표현, 가치관, 지속 가능성",
        "comparison": "선택 기준이 다른 학생들의 생각 차이",
        "solution": "더 합리적이고 책임 있게 선택하는 방법",
        "expert": "소비나 문화 경험에 대해 구체적으로 말할 수 있는 사람",
    },
]


def _question_profile(topic: str) -> dict:
    lowered = topic.lower()
    matches = []
    for profile in QUESTION_PROFILES:
        score = sum(1 for keyword in profile["keywords"] if keyword.lower() in lowered)
        if score > 0:
            matches.append((score, profile))
    matches.sort(key=lambda item: item[0], reverse=True)
    if len(matches) >= 2:
        primary = matches[0][1]
        secondary = matches[1][1]
        return {
            "experience": f"{primary['experience']} 또는 {secondary['experience']}",
            "factor": f"{primary['factor']} / {secondary['factor']}",
            "comparison": f"{primary['comparison']}와 {secondary['comparison']}",
            "solution": f"{primary['solution']}과 {secondary['solution']}",
            "expert": f"{primary['expert']} 또는 {secondary['expert']}",
        }
    if matches:
        return matches[0][1]
    return {
        "experience": "이 주제와 관련해 직접 겪거나 본 경험",
        "factor": "원인, 영향, 장단점, 학교생활과의 관련성",
        "comparison": "상황이나 사람에 따라 달라지는 점",
        "solution": "학교에서 실천할 수 있는 개선 방법",
        "expert": "이 주제와 관련된 경험이나 의견을 구체적으로 말할 수 있는 사람",
    }


def make_survey(topic: str) -> list[str]:
    profile = _question_profile(topic)
    return [
        f"'{topic}' 주제와 관련해 {profile['experience']}이 있나요?",
        f"'{topic}'에서 가장 중요하게 보아야 할 것은 무엇인가요? ({profile['factor']})",
        "이 주제가 나의 생활이나 학교생활에 어떤 영향을 준다고 생각하나요?",
        f"'{topic}'에 대해 {profile['comparison']}가 있다고 생각하나요?",
        f"'{topic}'을 더 잘 이해하려면 어떤 자료나 사례를 조사해야 한다고 생각하나요?",
        f"'{topic}'과 관련해 학교에서 실천할 수 있는 방법은 무엇인가요? ({profile['solution']})",
        "이 주제에 대해 추가로 말하고 싶은 의견이나 걱정되는 점을 적어 주세요.",
    ]


GUIDE_PROFILES = [
    {
        "keywords": ["AI", "인공지능", "알고리즘", "추천", "로봇", "자동화", "센서"],
        "source": "AI·기술 관련 기관 자료, 서비스 도움말, 기술 뉴스, 실제 활용 사례",
        "method": "기술이 어떤 데이터를 입력받고 어떤 판단이나 추천을 내리는지 과정도를 그려 본다.",
        "evidence": "정확도, 편리함, 개인정보, 공정성, 오류 가능성을 비교 기준으로 삼는다.",
        "keywords_hint": "검색어 예: 인공지능 추천 원리, 로봇 센서 활용, 알고리즘 공정성",
    },
    {
        "keywords": ["스포츠", "운동", "훈련", "경기", "자세", "부상", "기록"],
        "source": "스포츠 과학 자료, 경기 기록, 훈련 방법 소개 자료, 보건·체육 기관 자료",
        "method": "기록, 자세, 운동 전후 변화처럼 숫자로 비교할 수 있는 자료를 우선 찾는다.",
        "evidence": "기록 변화, 부상 예방, 참여도, 체력 요소를 기준으로 자료를 분류한다.",
        "keywords_hint": "검색어 예: 운동 기록 향상 요인, 스포츠 부상 예방, 자세 교정 방법",
    },
    {
        "keywords": ["유튜브", "영상", "미디어", "스마트폰", "SNS", "콘텐츠", "웹툰", "영화", "K-POP"],
        "source": "미디어 이용 통계, 플랫폼 정책, 청소년 미디어 연구, 콘텐츠 사례",
        "method": "시청 시간, 추천 방식, 댓글 반응, 정보 신뢰도처럼 관찰 가능한 항목을 정한다.",
        "evidence": "몰입도, 정보 신뢰성, 표현 방식, 청소년 생활 습관 영향을 비교한다.",
        "keywords_hint": "검색어 예: 청소년 미디어 이용 통계, 추천 알고리즘 영향, 콘텐츠 소비 습관",
    },
    {
        "keywords": ["환경", "탄소", "재활용", "쓰레기", "에너지", "기후", "동물", "생태"],
        "source": "환경부·지자체 자료, 공공 통계, 환경 캠페인 사례, 생태 관련 기사",
        "method": "우리 학교나 생활 주변에서 관찰할 수 있는 행동과 환경 변화를 연결해 조사한다.",
        "evidence": "자원 절약 효과, 실천 가능성, 비용, 지속 가능성을 기준으로 정리한다.",
        "keywords_hint": "검색어 예: 학교 재활용 실천, 탄소 배출 줄이기, 생활 속 환경 보호",
    },
    {
        "keywords": ["건강", "수면", "스트레스", "음식", "식생활", "급식", "보건"],
        "source": "보건복지부·질병관리청 자료, 식품영양 정보, 청소년 건강 통계",
        "method": "생활 습관, 식단, 수면, 스트레스처럼 설문으로 확인할 항목을 먼저 정한다.",
        "evidence": "건강 영향, 실천 난이도, 청소년에게 맞는 권장 기준을 비교한다.",
        "keywords_hint": "검색어 예: 청소년 수면 권장 시간, 건강한 식생활, 스트레스 관리 방법",
    },
    {
        "keywords": ["친구", "관계", "소통", "학교생활", "학습", "수업", "진로", "직업"],
        "source": "교육부 자료, 학교생활 연구, 진로 정보 사이트, 청소년 상담 자료",
        "method": "학생 경험을 설문·인터뷰로 모으고, 공식 자료와 비교해 공통점과 차이를 찾는다.",
        "evidence": "만족도, 갈등 원인, 학습 효과, 진로 역량, 학교 적용 가능성을 기준으로 본다.",
        "keywords_hint": "검색어 예: 학교생활 만족도, 또래 관계 갈등 해결, 청소년 진로 탐색",
    },
    {
        "keywords": ["패션", "소비", "쇼핑", "브랜드", "여행", "문화"],
        "source": "소비자원 자료, 문화·관광 통계, 브랜드 사례, 청소년 소비 관련 기사",
        "method": "선택 이유, 가격, 유행, 가치관처럼 의사결정에 영향을 주는 요인을 나눠 조사한다.",
        "evidence": "경제성, 자기표현, 문화적 의미, 지속 가능성을 비교 기준으로 삼는다.",
        "keywords_hint": "검색어 예: 청소년 소비 행동, 패션과 자기표현, 여행 문화 차이",
    },
]


def _guide_profile(topic: str) -> dict:
    lowered = topic.lower()
    matches = []
    for profile in GUIDE_PROFILES:
        score = sum(1 for keyword in profile["keywords"] if keyword.lower() in lowered)
        if score > 0:
            matches.append((score, profile))
    matches.sort(key=lambda item: item[0], reverse=True)
    if len(matches) >= 2:
        primary = matches[0][1]
        secondary = matches[1][1]
        return {
            "source": f"{primary['source']}와 {secondary['source']}",
            "method": f"{primary['method']} 또한 {secondary['method']}",
            "evidence": f"{primary['evidence']} 또한 {secondary['evidence']}",
            "keywords_hint": f"{primary['keywords_hint']} / {secondary['keywords_hint']}",
        }
    if matches:
        return matches[0][1]
    return {
        "source": "학교도서관, 공공기관 자료, 뉴스, 전문가 글처럼 출처가 분명한 자료",
        "method": "주제의 원인, 영향, 해결 방법을 나누어 자료를 찾고 서로 비교한다.",
        "evidence": "신뢰도, 학생 생활과의 관련성, 학교에서 실천할 가능성을 기준으로 정리한다.",
        "keywords_hint": f"검색어 예: {topic} 원인, {topic} 영향, {topic} 해결 방법",
    }


def _guide_inquiry_focus(topic: str) -> str:
    if any(word in topic for word in ["비교", "차이", "전후", "영향"]):
        return "비교할 집단이나 조건을 먼저 정하고, 같은 기준으로 자료를 모은다."
    if any(word in topic for word in ["해결", "개선", "제안", "캠페인", "아이디어"]):
        return "이미 시도된 해결 사례를 2가지 이상 찾고, 우리 학교에 맞게 바꿀 점을 표시한다."
    if any(word in topic for word in ["데이터", "통계", "분석", "기록"]):
        return "숫자로 정리할 수 있는 자료를 우선 모으고, 표와 그래프로 바꿀 항목을 정한다."
    if any(word in topic for word in ["윤리", "공정", "안전", "개인정보", "신뢰"]):
        return "찬성·반대 근거를 각각 찾고, 학생 입장에서 지켜야 할 기준을 정리한다."
    return "자료조사, 설문, 관찰 중 이 주제에 가장 잘 맞는 방법을 하나 정해 근거를 모은다."


def make_research_guide(topic: str) -> list[str]:
    profile = _guide_profile(topic)
    focus = _guide_inquiry_focus(topic)
    return [
        f"'{topic}'와 직접 관련된 자료를 찾기 위해 {profile['source']}를 우선 확인한다.",
        profile["keywords_hint"],
        profile["method"],
        focus,
        f"자료를 읽을 때 {profile['evidence']}",
        "자료마다 작성자, 날짜, 기관, 링크를 기록하고 최신 자료인지 확인한다.",
        "마지막에는 찾은 자료가 탐구 문제에 답하는 데 충분한지 보고, 부족하면 설문이나 인터뷰 질문을 보완한다.",
    ]


def make_interview(topic: str) -> list[str]:
    profile = _question_profile(topic)
    return [
        f"'{topic}' 주제와 관련해 직접 겪었거나 본 경험을 구체적으로 말해 주세요.",
        f"그 경험에서 가장 중요하다고 느낀 점은 무엇인가요? ({profile['factor']})",
        "이 주제에서 문제가 생긴다면 가장 큰 원인은 무엇이라고 생각하나요?",
        f"'{topic}'에 대해 {profile['comparison']}를 확인하려면 어떤 자료나 사례가 필요할까요?",
        f"학교에서 이 주제를 개선하거나 활용하려면 어떤 방법이 현실적일까요? ({profile['solution']})",
        f"이 주제를 조사할 때 {profile['expert']}에게 꼭 물어봐야 할 질문은 무엇일까요?",
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
