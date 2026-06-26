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

CUSTOM_INTEREST_KEYWORDS = [
    (["축구", "농구", "야구", "배구", "탁구", "배드민턴", "수영", "달리기", "태권도", "운동", "스포츠"], "스포츠"),
    (["게임", "로블록스", "마인크래프트", "브롤스타즈", "피파", "롤", "오버워치"], "게임"),
    (["유튜브", "영상", "쇼츠", "틱톡", "인스타", "SNS", "인플루언서"], "유튜브"),
    (["웹툰", "만화"], "웹툰"),
    (["영화", "드라마", "애니"], "영화"),
    (["노래", "음악", "악기", "밴드", "랩", "댄스"], "음악"),
    (["아이돌", "케이팝", "KPOP", "K-POP"], "K-POP"),
    (["AI", "인공지능", "챗GPT", "챗지피티"], "AI"),
    (["로봇", "드론", "코딩", "프로그래밍"], "로봇"),
    (["환경", "기후", "분리수거", "플라스틱", "제로웨이스트"], "환경"),
    (["건강", "수면", "스트레스", "식습관", "다이어트"], "건강"),
    (["친구", "우정", "관계", "소통"], "친구관계"),
    (["진로", "직업", "꿈"], "진로"),
    (["공부", "학습", "시험", "수업"], "학교생활"),
]

DOMAIN_PAIR_TEMPLATES = {
    ("스포츠", "스포츠"): [
        ("{first}와 {second} 참여 학생의 운동 동기와 지속 요인 비교", "체육", "중", "설문형", 3),
        ("{first}와 {second}에서 팀워크가 경기 만족도에 미치는 영향", "사회", "중", "설문형", 3),
        ("{first}와 {second}의 부상 예방 습관과 준비운동 실천 비교", "체육", "중", "자료조사형", 3),
        ("중학생이 {first}와 {second} 중 하나를 선택할 때 중요하게 보는 기준 분석", "체육", "하", "설문형", 2),
        ("학교 체육 시간에 {first}와 {second}를 더 안전하고 재미있게 운영하는 방법 제안", "체육", "중", "실천형", 4),
    ],
    ("게임", "스포츠"): [
        ("스포츠 게임 경험이 실제 {second} 참여 흥미에 미치는 영향", "체육", "중", "설문형", 3),
        ("게임 속 전략 이해가 {second} 경기 관찰과 팀 전술 이해에 주는 도움", "체육", "중", "인터뷰형", 3),
        ("온라인 게임의 경쟁 경험과 실제 운동 경기의 협동 태도 비교", "도덕", "중", "설문형", 3),
    ],
    ("유튜브", "스포츠"): [
        ("스포츠 영상 시청이 {second} 연습 방법 선택에 미치는 영향", "체육", "중", "설문형", 3),
        ("유튜브 운동 콘텐츠의 장점과 부상 위험 정보 신뢰도 분석", "정보", "중", "자료조사형", 3),
        ("중학생이 스포츠 영상을 보고 실제 운동을 따라 할 때 필요한 안전 기준 만들기", "체육", "중", "실천형", 3),
    ],
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


def _topic_variation(topic: str, salt: int) -> int:
    value = sum((index + 1 + salt) * ord(ch) for index, ch in enumerate(topic))
    return value % 13 - 6


def _keyword_score(topic: str, keywords: list[str], weight: int = 4) -> int:
    return sum(weight for keyword in keywords if keyword.lower() in topic.lower())


def fit_scores(topic: str, inquiry_type: str = "", difficulty: str = "중", weeks: int = 3) -> dict:
    data = 66
    survey = 58
    experiment = 42
    school = 64
    if inquiry_type == "설문형":
        survey += 22
        school += 8
    elif inquiry_type == "자료조사형":
        data += 23
    elif inquiry_type == "분석형":
        data += 16
        survey += 7
        experiment += 3
    elif inquiry_type == "실천형":
        school += 22
        survey += 4
    elif inquiry_type == "실험형":
        experiment += 28
        data += 4
    elif inquiry_type == "인터뷰형":
        survey += 17
        data += 9

    data += _keyword_score(topic, ["자료", "사례", "뉴스", "통계", "데이터", "분석", "비교", "원리", "신뢰도"], 3)
    survey += _keyword_score(topic, ["인식", "선호", "만족도", "경험", "생각", "의견", "친구", "기대", "걱정"], 3)
    experiment += _keyword_score(topic, ["실험", "관찰", "전후", "변화", "기록", "효과", "원리", "훈련", "센서"], 4)
    school += _keyword_score(topic, ["학교", "학급", "학생", "중학생", "캠페인", "생활", "실천", "수업", "동아리"], 3)

    if difficulty == "하":
        survey += 4
        school += 6
        experiment -= 4
    elif difficulty == "상":
        data += 5
        experiment += 6
        school -= 3

    if weeks <= 2:
        school += 4
        data -= 3
    elif weeks >= 5:
        data += 4
        experiment += 5
        school -= 2

    data += _topic_variation(topic, 1)
    survey += _topic_variation(topic, 5)
    experiment += _topic_variation(topic, 9)
    school += _topic_variation(topic, 13)

    vals = [max(20, min(98, round(x))) for x in [data, survey, experiment, school]]
    total = round(vals[0] * 0.30 + vals[1] * 0.25 + vals[2] * 0.20 + vals[3] * 0.25)
    return {
        "data_collection": vals[0],
        "survey": vals[1],
        "experiment": vals[2],
        "school_application": vals[3],
        "total": max(20, min(98, total)),
    }


def _split_tags(tag: str) -> list[str]:
    return [part.strip() for part in tag.split("+") if part.strip()]


def _split_interests(value: str) -> list[str]:
    normalized = value.replace("，", ",").replace("、", ",").replace("+", ",")
    return [part.strip() for part in normalized.split(",") if part.strip()]


def _category_for_interest(name: str) -> str:
    if name in INTEREST_PROFILES:
        return name
    lowered = name.lower()
    for keywords, category in CUSTOM_INTEREST_KEYWORDS:
        if any(keyword.lower() in lowered for keyword in keywords):
            return category
    return ""


def _profile_for_interest(name: str) -> tuple[str, str]:
    category = _category_for_interest(name)
    if category:
        base_domain, base_focus = INTEREST_PROFILES[category]
        if name == category:
            return base_domain, base_focus
        return f"{name} 관련 {base_domain}", base_focus
    return f"{name} 경험과 선택", "참여 이유, 선호 기준, 생활 속 영향"


def _profile(name: str) -> tuple[str, str]:
    return INTEREST_PROFILES.get(name, (name, "학생들의 생각, 생활 변화, 학교 적용 가능성"))


def _fusion_context(interests: list[str]) -> dict:
    first = interests[0] if interests else "학교생활"
    second = interests[1] if len(interests) > 1 else first
    a_domain, a_focus = _profile_for_interest(first)
    b_domain, b_focus = _profile_for_interest(second)
    if first != second:
        context = f"{first}와 {second}가 학생 생활에서 연결되는 지점"
    else:
        context = f"{a_domain}과 {b_domain}이 만나는 생활 속 장면"
    return {
        "first": first,
        "second": second,
        "a_domain": a_domain,
        "a_focus": a_focus,
        "b_domain": b_domain,
        "b_focus": b_focus,
        "context": context,
    }


def _pair_key(first: str, second: str) -> tuple[str, str]:
    a = _category_for_interest(first)
    b = _category_for_interest(second)
    if not a or not b:
        return ("", "")
    if (a, b) in DOMAIN_PAIR_TEMPLATES:
        return (a, b)
    if (b, a) in DOMAIN_PAIR_TEMPLATES:
        return (b, a)
    return (a, b)


def _swap_first_second(template: str) -> str:
    return template.replace("{first}", "{__tmp__}").replace("{second}", "{first}").replace("{__tmp__}", "{second}")


def _pair_templates(first: str, second: str) -> list[tuple[str, str, str, str, int]]:
    key = _pair_key(first, second)
    templates = DOMAIN_PAIR_TEMPLATES.get(key, [])
    if not templates:
        return []
    if key[0] != _category_for_interest(first):
        return [
            (_swap_first_second(template), subject, difficulty, inquiry_type, weeks)
            for template, subject, difficulty, inquiry_type, weeks in templates
        ]
    return templates


def recommend_topics(tag: str, detail: str) -> list[dict]:
    tags = _split_tags(tag.strip())
    detail = detail.strip()
    detail_items = _split_interests(detail)
    interests = (tags + detail_items)[:2]
    is_fusion = len(interests) >= 2

    items = []
    if is_fusion:
        context = _fusion_context(interests)
        pair_specific_templates = _pair_templates(context["first"], context["second"])
        templates = pair_specific_templates + FUSION_TEMPLATES
        seen_topics = set()
        for index, (template, subject, difficulty, inquiry_type, weeks) in enumerate(templates):
            topic = template.format(**context)
            if topic in seen_topics:
                continue
            seen_topics.add(topic)
            fit = fit_scores(topic, inquiry_type, difficulty, weeks)
            if index < len(pair_specific_templates):
                for key in ["data_collection", "survey", "experiment", "school_application"]:
                    fit[key] = min(98, fit[key] + 8)
                fit["total"] = min(98, fit["total"] + 10)
            items.append({
                "topic": topic,
                "subject": subject,
                "difficulty": difficulty,
                "inquiry_type": inquiry_type,
                "duration": f"{weeks}주",
                "reason": f"'{context['first']}'와 '{context['second']}'를 단순히 붙이지 않고, '{context['context']}'에서 조사할 수 있는 문제로 바꾼 주제입니다.",
                "fit": fit,
            })
    else:
        interest = detail or (tags[0] if tags else "학교생활")
        for template, subject, difficulty, inquiry_type, weeks in SINGLE_TEMPLATES:
            topic = template.format(interest=interest)
            fit = fit_scores(topic, inquiry_type, difficulty, weeks)
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


TOPIC_METHOD_HINTS = {
    "비교": ("설문형", "중", "두 집단이나 두 상황을 같은 기준으로 비교한다."),
    "영향": ("설문형", "중", "원인으로 볼 항목과 결과로 볼 항목을 나누어 관계를 살핀다."),
    "개선": ("실천형", "중", "문제 원인을 찾고 학교에서 실행 가능한 해결 방안을 제안한다."),
    "안전": ("자료조사형", "중", "위험 요인과 예방 기준을 실제 사례와 함께 정리한다."),
    "윤리": ("자료조사형", "상", "찬반 근거와 학생이 지켜야 할 기준을 함께 검토한다."),
    "자료": ("분석형", "상", "수집 가능한 수치나 사례를 표로 정리해 경향을 분석한다."),
    "선택": ("설문형", "하", "선택 기준과 선호 이유를 설문으로 확인한다."),
}


def _clean_interest_parts(tag: str, detail: str) -> list[str]:
    raw = []
    raw.extend(_split_tags(tag.strip()))
    raw.extend(_split_interests(detail.strip()))
    cleaned = []
    for item in raw:
        name = " ".join(item.split())
        if name and name not in cleaned:
            cleaned.append(name)
    return cleaned[:2]


def _interest_info(name: str) -> dict:
    category = _category_for_interest(name) or name
    domain, focus = _profile_for_interest(name)
    return {
        "name": name,
        "category": category,
        "domain": domain,
        "focus": focus,
    }


def _topic_kind(topic: str) -> str:
    checks = [
        ("안전", ["안전", "부상", "위험", "예방"]),
        ("윤리", ["윤리", "공정", "신뢰", "개인정보", "기준"]),
        ("개선", ["개선", "제안", "만들기", "운영", "캠페인", "방법"]),
        ("자료", ["자료", "데이터", "분석", "기록", "경향"]),
        ("비교", ["비교", "차이"]),
        ("영향", ["영향", "미치는"]),
        ("선택", ["선택", "기준", "선호"]),
    ]
    for kind, words in checks:
        if any(word in topic for word in words):
            return kind
    return "영향"


def _make_topic(topic: str, subject: str, kind: str, weeks: int, reason: str, boost: int = 0) -> dict:
    inquiry_type, difficulty, _ = TOPIC_METHOD_HINTS.get(kind, TOPIC_METHOD_HINTS["영향"])
    fit = fit_scores(topic, inquiry_type, difficulty, weeks)
    fit["total"] = max(20, min(98, fit["total"] + boost))
    return {
        "topic": topic,
        "subject": subject,
        "difficulty": difficulty,
        "inquiry_type": inquiry_type,
        "duration": f"{weeks}주",
        "reason": reason,
        "fit": fit,
    }


def _subject_for(info: dict) -> str:
    category = info["category"]
    return {
        "스포츠": "체육",
        "게임": "정보",
        "유튜브": "정보",
        "스마트폰": "정보",
        "AI": "정보",
        "로봇": "기술",
        "건강": "보건",
        "환경": "과학",
        "친구관계": "도덕",
        "진로": "진로",
        "웹툰": "국어",
        "영화": "국어",
        "음악": "음악",
        "K-POP": "사회",
        "패션": "사회",
        "음식": "보건",
        "학교생활": "사회",
    }.get(category, "사회")


def _pair_label(first: str, second: str) -> str:
    return f"{first}·{second}"


def _single_interest_topics(info: dict) -> list[dict]:
    n = info["name"]
    d = info["domain"]
    f = info["focus"]
    subject = _subject_for(info)
    reason = f"'{n}'을 중학생이 실제로 조사할 수 있는 생활 문제로 바꾼 주제입니다."
    return [
        _make_topic(f"중학생의 {n} 관심도와 참여 이유 분석", subject, "선택", 3, reason, 8),
        _make_topic(f"{n} 경험이 학교생활 만족도와 친구 관계에 미치는 영향", "사회", "영향", 3, reason, 7),
        _make_topic(f"{n}을 더 안전하고 건강하게 즐기기 위한 학생 기준 만들기", "도덕", "안전", 3, reason, 6),
        _make_topic(f"{d}에서 학생들이 중요하게 보는 {f} 요인 비교", subject, "비교", 3, reason, 5),
        _make_topic(f"학교에서 {n} 관심을 활용한 작은 활동 또는 캠페인 제안", "진로", "개선", 4, reason, 4),
        _make_topic(f"{n} 관련 자료와 학생 설문을 바탕으로 한 인식 차이 분석", "사회", "자료", 4, reason, 3),
    ]


def _fusion_interest_topics(a: dict, b: dict) -> list[dict]:
    first = a["name"]
    second = b["name"]
    pair = _pair_label(first, second)
    a_cat = a["category"]
    b_cat = b["category"]
    reason = f"'{first}'와 '{second}'를 단순히 나열하지 않고, 학생 생활에서 두 관심사가 만나는 지점을 탐구 문제로 바꾼 주제입니다."
    topics = []

    if a_cat == b_cat:
        subject = _subject_for(a)
        topics.extend([
            _make_topic(f"{pair} 중학생 선택 기준과 선호 이유 비교", subject, "비교", 3, reason, 10),
            _make_topic(f"{pair} 참여 경험이 친구 관계와 학교생활 만족도에 미치는 영향", "사회", "영향", 3, reason, 9),
            _make_topic(f"{pair} 활동을 더 안전하고 지속적으로 즐기기 위한 실천 기준 만들기", subject, "안전", 3, reason, 8),
        ])
    else:
        topics.extend([
            _make_topic(f"{first} 경험이 {second}에 대한 관심과 참여 방식에 미치는 영향", _subject_for(b), "영향", 3, reason, 10),
            _make_topic(f"{pair} 모두에 관심 있는 학생들의 공통 특징 분석", "사회", "자료", 4, reason, 9),
            _make_topic(f"{first} 관심을 활용해 {second} 활동을 더 효과적으로 돕는 방법 제안", "진로", "개선", 4, reason, 8),
        ])

    pair_categories = {a_cat, b_cat}
    if pair_categories & {"유튜브", "스마트폰", "게임"}:
        other = second if a_cat in {"유튜브", "스마트폰", "게임"} else first
        topics.append(_make_topic(f"온라인 콘텐츠가 {other}에 대한 정보 신뢰도와 선택에 미치는 영향", "정보", "윤리", 4, reason, 8))
    if pair_categories & {"AI", "로봇"}:
        other = second if a_cat in {"AI", "로봇"} else first
        topics.append(_make_topic(f"AI와 기술을 활용해 {other} 활동을 도울 때 필요한 공정성과 안전 기준", "정보", "윤리", 4, reason, 8))
    if pair_categories & {"건강", "스포츠", "음식"}:
        topics.append(_make_topic(f"{pair} 관심이 건강한 생활 습관 형성에 주는 도움과 한계", "보건", "영향", 3, reason, 7))
    if pair_categories & {"친구관계", "학교생활"}:
        topics.append(_make_topic(f"{pair} 관심이 학급 소통과 협력에 미치는 영향", "도덕", "영향", 3, reason, 7))
    if pair_categories & {"환경"}:
        topics.append(_make_topic(f"{pair} 관심을 환경 보호 실천과 연결하는 학교 캠페인 제안", "과학", "개선", 4, reason, 7))

    topics.extend([
        _make_topic(f"학교에서 {pair} 관심을 함께 살린 탐구 활동 설계", "진로", "개선", 4, reason, 5),
        _make_topic(f"{pair} 관련 학생 경험을 설문과 인터뷰로 비교 분석하기", "사회", "비교", 3, reason, 4),
    ])
    return topics


def _dedupe_and_rank(items: list[dict]) -> list[dict]:
    seen = set()
    ranked = []
    for item in items:
        topic = item["topic"]
        if topic in seen:
            continue
        seen.add(topic)
        ranked.append(item)
    ranked.sort(key=lambda x: x["fit"]["total"], reverse=True)
    return ranked[:20]


def recommend_topics(tag: str, detail: str) -> list[dict]:
    interests = _clean_interest_parts(tag, detail)
    if len(interests) >= 2:
        items = _fusion_interest_topics(_interest_info(interests[0]), _interest_info(interests[1]))
    elif len(interests) == 1:
        items = _single_interest_topics(_interest_info(interests[0]))
    else:
        items = _single_interest_topics(_interest_info("학교생활"))
    return _dedupe_and_rank(items)


def _topic_terms(topic: str) -> list[str]:
    terms = []
    known_terms = list(INTEREST_PROFILES.keys())
    for keywords, _ in CUSTOM_INTEREST_KEYWORDS:
        known_terms.extend(keywords)
    for keyword in sorted(set(known_terms), key=len, reverse=True):
        if keyword and keyword in topic and keyword not in terms:
            terms.append(keyword)
        if len(terms) >= 4:
            return terms
    for chunk in topic.replace("·", ",").replace("와", ",").replace("과", ",").replace("을", ",").replace("를", ",").replace("에", ",").split(","):
        cleaned = "".join(ch for ch in chunk.strip() if ch.isalnum() or ch in " -")
        if 2 <= len(cleaned) <= 12 and cleaned not in terms:
            terms.append(cleaned)
    return terms[:4]


def _topic_guidance(topic: str) -> dict:
    kind = _topic_kind(topic)
    terms = _topic_terms(topic)
    main = terms[0] if terms else topic
    second = terms[1] if len(terms) > 1 else "학교생활"
    inquiry_type, _, method_hint = TOPIC_METHOD_HINTS.get(kind, TOPIC_METHOD_HINTS["영향"])
    return {
        "kind": kind,
        "main": main,
        "second": second,
        "method_hint": method_hint,
        "inquiry_type": inquiry_type,
    }


def make_research_guide(topic: str) -> list[str]:
    g = _topic_guidance(topic)
    return [
        f"핵심 개념을 먼저 정리하세요: '{g['main']}', '{g['second']}', 그리고 주제 속 '{g['kind']}'이 무엇을 뜻하는지 학생 눈높이로 정의합니다.",
        f"자료는 3곳만 우선 찾으세요: 공공기관/학교 자료 1개, 최근 기사나 통계 1개, 학생 생활 사례 1개를 골라 이 주제와 직접 연결되는 부분만 기록합니다.",
        f"조사 방향은 '{g['method_hint']}'입니다. 자료를 읽을 때 원인, 결과, 비교 기준, 학교 적용 가능성을 표로 나누어 정리합니다.",
        f"마지막에는 자료조사로 부족한 점을 하나 찾고, 그것을 설문 또는 인터뷰 질문으로 바꿉니다. 예: '{topic}'에서 학생에게 직접 확인해야 할 생각이나 경험은 무엇인가?",
    ]


def make_survey(topic: str) -> list[str]:
    g = _topic_guidance(topic)
    if g["kind"] == "비교":
        return [
            f"'{topic}'에서 비교하려는 두 대상 중 어느 쪽에 더 관심이 있나요? 그 이유는 무엇인가요?",
            f"두 대상을 비교할 때 가장 중요하다고 생각하는 기준은 무엇인가요? 예: 재미, 도움, 안전, 친구와 함께하기, 지속 가능성",
            f"본인의 경험을 기준으로 두 대상의 장점과 불편한 점을 각각 하나씩 적어 주세요.",
            f"학교에서 이 주제를 활용한다면 어떤 방식이 가장 현실적이라고 생각하나요?",
        ]
    if g["kind"] == "개선":
        return [
            f"'{topic}'과 관련해 현재 가장 불편하거나 아쉬운 점은 무엇인가요?",
            "그 문제가 생기는 가장 큰 이유는 무엇이라고 생각하나요?",
            "제안된 해결 방법이 실제 학교에서 가능하려면 어떤 조건이 필요할까요?",
            "이 주제를 개선하면 학생들에게 어떤 변화가 생길 것이라고 생각하나요?",
        ]
    if g["kind"] in {"안전", "윤리"}:
        return [
            f"'{topic}'과 관련해 가장 걱정되는 점은 무엇인가요?",
            "안전하거나 공정하게 이용하기 위해 가장 중요한 기준은 무엇이라고 생각하나요?",
            "친구들이 이 기준을 잘 지키지 못하는 이유가 있다면 무엇일까요?",
            "학교나 학급에서 만들 수 있는 약속 또는 안내 문구를 하나 제안해 주세요.",
        ]
    if g["kind"] == "자료":
        return [
            f"'{topic}'에서 공통 특징으로 확인하고 싶은 항목은 무엇인가요? 예: 시간, 이유, 함께하는 사람, 장점, 어려움",
            "본인은 이 주제와 관련해 어떤 경험이나 관심을 가지고 있나요?",
            "비슷한 관심을 가진 친구들에게서 공통적으로 나타날 것 같은 특징은 무엇이라고 예상하나요?",
            "조사 결과를 표나 그래프로 정리한다면 어떤 기준으로 나누는 것이 좋을까요?",
        ]
    return [
        f"'{topic}'과 관련한 경험이 있나요? 있다면 어떤 경험인가요?",
        f"이 주제가 본인의 생활이나 학교생활에 어느 정도 영향을 준다고 생각하나요? 이유도 적어 주세요.",
        "영향을 주는 가장 중요한 요인은 무엇이라고 생각하나요? 예: 시간, 친구, 정보, 규칙, 건강, 재미",
        "조사 결과를 바탕으로 학교에서 실천할 수 있는 방법을 하나 제안해 주세요.",
    ]


def make_interview(topic: str) -> list[str]:
    g = _topic_guidance(topic)
    return [
        f"'{topic}' 주제와 관련해 직접 경험했거나 주변에서 본 장면을 구체적으로 말해 주세요.",
        f"그 경험에서 가장 중요하게 작용한 요인은 무엇이었나요? 왜 그렇게 생각하나요?",
        f"이 주제를 조사할 때 설문만으로는 알기 어려운 부분은 무엇이라고 보나요?",
        f"학생들이 실제로 실천할 수 있는 개선 방법이나 주의할 점을 하나 제안한다면 무엇인가요?",
    ]


REPORT_PROFILES = [
    {
        "keywords": ["AI", "인공지능", "알고리즘", "추천", "로봇", "자동화", "센서"],
        "background": "기술이 편리함을 주는 동시에 오류, 개인정보, 공정성 문제를 만들 수 있다는 점",
        "research_focus": "학생들이 기술의 장점과 위험을 어떻게 인식하는지, 실제 사용 경험이 판단에 어떤 영향을 주는지",
        "data_hint": "서비스 사용 경험 설문, 기술 원리 자료, 실제 활용 사례, 오류나 부작용 사례",
        "analysis_frame": "편리함, 정확성, 안전성, 공정성 기준으로 응답을 나누어 비교한다.",
        "visual_hint": "장점과 걱정 요인을 막대그래프로 비교하고, 사용 경험 유무에 따른 차이를 표로 정리한다.",
        "proposal": "학생용 사용 기준, 개인정보 보호 수칙, 학교에서 안전하게 활용하는 절차",
    },
    {
        "keywords": ["스포츠", "운동", "훈련", "경기", "자세", "부상", "기록"],
        "background": "운동 참여와 훈련 방식이 흥미, 기록, 안전에 직접적인 영향을 줄 수 있다는 점",
        "research_focus": "학생들이 어떤 훈련 방법을 선호하고, 기록 향상이나 부상 예방에 어떤 요인이 중요하다고 보는지",
        "data_hint": "운동 경험 설문, 기록 변화 관찰, 훈련 방법 자료, 부상 예방 자료",
        "analysis_frame": "기록 향상, 흥미, 안전, 지속 가능성 기준으로 자료와 응답을 비교한다.",
        "visual_hint": "운동 빈도와 만족도, 부상 경험과 안전 수칙 인식의 관계를 그래프로 나타낸다.",
        "proposal": "학교 체육 활동에서 실천할 수 있는 준비운동, 안전 수칙, 훈련 방법 개선안",
    },
    {
        "keywords": ["유튜브", "영상", "미디어", "스마트폰", "SNS", "콘텐츠", "웹툰", "영화", "K-POP"],
        "background": "미디어와 콘텐츠 이용이 즐거움, 정보 습득, 생활 습관, 친구 관계에 영향을 줄 수 있다는 점",
        "research_focus": "학생들이 콘텐츠를 이용하는 이유와 시간, 긍정적 효과와 부정적 영향을 어떻게 느끼는지",
        "data_hint": "이용 시간 설문, 콘텐츠 유형별 선호도, 청소년 미디어 이용 통계, 사례 분석",
        "analysis_frame": "이용 목적, 이용 시간, 만족도, 생활 습관 변화, 정보 신뢰도 기준으로 응답을 분류한다.",
        "visual_hint": "이용 시간대별 응답 비율과 긍정·부정 영향 순위를 그래프로 정리한다.",
        "proposal": "건강한 이용 시간, 비판적 콘텐츠 읽기, 친구와 함께 지킬 수 있는 이용 약속",
    },
    {
        "keywords": ["환경", "탄소", "재활용", "쓰레기", "에너지", "기후", "동물", "생태"],
        "background": "생활 속 작은 선택이 자원 사용, 쓰레기, 생태 환경에 누적된 영향을 줄 수 있다는 점",
        "research_focus": "학생들이 환경 문제를 얼마나 체감하고, 학교에서 어떤 실천을 현실적으로 할 수 있다고 보는지",
        "data_hint": "학교 주변 관찰 기록, 실천 경험 설문, 공공기관 환경 자료, 캠페인 사례",
        "analysis_frame": "실천 가능성, 효과, 비용, 지속 가능성 기준으로 해결 방안을 비교한다.",
        "visual_hint": "가장 많이 실천하는 행동과 실천이 어려운 이유를 원형 또는 막대그래프로 나타낸다.",
        "proposal": "교실·급식실·동아리에서 바로 실행할 수 있는 환경 실천 캠페인",
    },
    {
        "keywords": ["건강", "수면", "스트레스", "음식", "식생활", "급식", "보건"],
        "background": "수면, 식생활, 스트레스 관리 같은 습관이 학습 집중도와 학교생활 만족도에 영향을 줄 수 있다는 점",
        "research_focus": "학생들의 생활 습관이 어떤 상태이며, 스스로 느끼는 건강과 학교생활에 어떤 차이를 만드는지",
        "data_hint": "생활 습관 설문, 청소년 건강 권장 기준, 식생활·수면 관련 공공 자료",
        "analysis_frame": "습관 실천 정도, 어려움, 건강 영향, 학습 집중도 기준으로 응답을 비교한다.",
        "visual_hint": "수면 시간 또는 식습관 유형에 따른 만족도 차이를 표와 그래프로 정리한다.",
        "proposal": "중학생이 무리 없이 실천할 수 있는 건강 습관 체크리스트",
    },
    {
        "keywords": ["친구", "관계", "소통", "학교생활", "학습", "수업", "진로", "직업"],
        "background": "학교생활 경험과 관계, 학습, 진로 인식이 학생의 만족도와 참여도에 영향을 줄 수 있다는 점",
        "research_focus": "학생들이 학교생활에서 어떤 어려움과 도움 요인을 느끼는지, 개선이 필요한 지점은 무엇인지",
        "data_hint": "학생 경험 설문, 인터뷰, 학교생활 관련 자료, 진로 정보 자료",
        "analysis_frame": "만족도, 어려움, 도움 요인, 개선 요구, 학교 적용 가능성 기준으로 응답을 나눈다.",
        "visual_hint": "만족도가 높은 학생과 낮은 학생의 응답 차이를 비교표로 정리한다.",
        "proposal": "학급 규칙, 친구 관계, 학습 지원, 진로 활동을 개선하는 실천 제안",
    },
    {
        "keywords": ["패션", "소비", "쇼핑", "브랜드", "여행", "문화"],
        "background": "소비와 문화 선택이 자기표현, 가치관, 비용, 지속 가능성과 연결될 수 있다는 점",
        "research_focus": "학생들이 무엇을 기준으로 선택하고 소비하는지, 유행과 가치관이 선택에 어떤 영향을 주는지",
        "data_hint": "선택 기준 설문, 소비 사례 조사, 문화 자료, 가격·브랜드 비교 자료",
        "analysis_frame": "가격, 유행, 자기표현, 필요성, 지속 가능성 기준으로 응답을 비교한다.",
        "visual_hint": "선택 기준의 우선순위와 소비 전후 만족도를 그래프로 정리한다.",
        "proposal": "합리적이고 책임 있는 선택을 돕는 학생용 판단 기준",
    },
]


def _report_profile(topic: str) -> dict:
    lowered = topic.lower()
    matches = []
    for profile in REPORT_PROFILES:
        score = sum(1 for keyword in profile["keywords"] if keyword.lower() in lowered)
        if score > 0:
            matches.append((score, profile))
    matches.sort(key=lambda item: item[0], reverse=True)
    if len(matches) >= 2:
        primary = matches[0][1]
        secondary = matches[1][1]
        return {
            "background": f"{primary['background']}과 {secondary['background']}",
            "research_focus": f"{primary['research_focus']} 또한 {secondary['research_focus']}",
            "data_hint": f"{primary['data_hint']} / {secondary['data_hint']}",
            "analysis_frame": f"{primary['analysis_frame']} 또한 {secondary['analysis_frame']}",
            "visual_hint": f"{primary['visual_hint']} 필요하면 {secondary['visual_hint']}",
            "proposal": f"{primary['proposal']}과 {secondary['proposal']}",
        }
    if matches:
        return matches[0][1]
    return {
        "background": "이 주제가 학생 생활과 학교 문제를 이해하는 데 도움을 줄 수 있다는 점",
        "research_focus": "학생들이 이 주제를 어떻게 경험하고 인식하는지, 학교생활과 어떤 관련이 있는지",
        "data_hint": "관련 자료, 학생 설문, 인터뷰, 학교에서 관찰할 수 있는 사례",
        "analysis_frame": "원인, 영향, 장단점, 실천 가능성 기준으로 자료와 응답을 비교한다.",
        "visual_hint": "응답 비율과 주요 의견을 표와 그래프로 정리한다.",
        "proposal": "학교나 학급에서 실천할 수 있는 현실적인 개선 방안",
    }


def _report_inquiry_shape(topic: str) -> dict:
    if any(word in topic for word in ["비교", "차이", "전후"]):
        return {
            "question": f"'{topic}'에서 비교 대상 사이에는 어떤 차이가 나타나는가?",
            "method": "비교할 두 집단이나 조건을 정하고, 같은 질문과 기준으로 자료를 모은다.",
            "analysis": "두 집단의 공통점과 차이점을 먼저 정리한 뒤, 차이가 생긴 이유를 해석한다.",
        }
    if any(word in topic for word in ["영향", "미치는"]):
        return {
            "question": f"'{topic}'에서 영향을 주는 요인과 영향을 받는 결과는 무엇인가?",
            "method": "원인으로 볼 수 있는 항목과 결과로 볼 수 있는 항목을 나누어 설문과 자료조사를 진행한다.",
            "analysis": "응답 결과가 높은 항목을 중심으로 영향의 방향과 이유를 설명한다.",
        }
    if any(word in topic for word in ["개선", "해결", "제안", "캠페인", "아이디어"]):
        return {
            "question": f"'{topic}'을 학교 상황에 맞게 실천하려면 어떤 조건이 필요할까?",
            "method": "문제 원인, 기존 해결 사례, 학생들이 실천 가능하다고 보는 방법을 함께 조사한다.",
            "analysis": "효과가 커 보이는 방법과 실제로 실천하기 쉬운 방법을 구분해 평가한다.",
        }
    if any(word in topic for word in ["데이터", "통계", "분석", "기록"]):
        return {
            "question": f"'{topic}'에서 숫자로 확인할 수 있는 경향은 무엇인가?",
            "method": "응답이나 관찰 결과를 표로 만들고, 평균·비율·순위처럼 비교 가능한 값으로 정리한다.",
            "analysis": "가장 두드러진 수치와 예상과 달랐던 수치를 중심으로 의미를 해석한다.",
        }
    if any(word in topic for word in ["윤리", "공정", "안전", "신뢰"]):
        return {
            "question": f"'{topic}'에서 학생들이 중요하게 생각해야 할 기준은 무엇인가?",
            "method": "찬성·반대 근거, 걱정되는 점, 필요한 규칙을 자료조사와 설문으로 확인한다.",
            "analysis": "편리함과 위험, 개인의 자유와 공동체 안전 사이의 균형을 중심으로 해석한다.",
        }
    return {
        "question": f"'{topic}'에 대해 학생들은 어떤 경험과 생각을 가지고 있는가?",
        "method": "자료조사로 배경을 확인하고, 설문이나 인터뷰로 학생 의견을 모은다.",
        "analysis": "가장 많이 나온 의견과 서로 다른 의견을 나누어 정리한다.",
    }


def _student_notes(log: str) -> str:
    text = (log or "").strip()
    if not text:
        return "아직 탐구일지가 충분하지 않습니다. 설문 결과, 인터뷰 내용, 조사한 자료의 핵심 문장을 여기에 추가하세요."
    return text


def _plan_excerpt(plan_text: str) -> str:
    text = (plan_text or "").strip()
    if not text:
        return "아직 탐구계획서가 충분하지 않습니다. 탐구 동기, 탐구 문제, 탐구 방법을 먼저 채운 뒤 보고서를 보완하세요."
    if len(text) <= 600:
        return text
    return text[:600].rstrip() + "\n...(계획서의 나머지 내용은 필요한 부분만 골라 보고서에 반영하세요.)"


def make_report(topic: str, plan_text: str, log: str) -> str:
    profile = _report_profile(topic)
    shape = _report_inquiry_shape(topic)
    notes = _student_notes(log)
    plan = _plan_excerpt(plan_text)
    return f"""# 탐구 보고서 초안

## 1. 탐구 주제
{topic}

## 2. 탐구 동기
이 주제는 {profile['background']}에서 출발했다. 특히 내 주변 학생들의 실제 경험과 생각을 확인하면, 막연한 느낌이 아니라 근거를 바탕으로 문제를 이해할 수 있다고 보았다.

## 3. 탐구 문제
{shape['question']}

세부적으로는 {profile['research_focus']}를 중심으로 살펴본다.

## 4. 탐구 방법
1. 자료조사: {profile['data_hint']}를 찾아 주제의 배경과 핵심 개념을 정리한다.
2. 설문/인터뷰: {shape['method']}
3. 결과 정리: {profile['visual_hint']}
4. 해석 기준: {profile['analysis_frame']}

## 5. 기존 탐구계획서에서 가져올 내용
{plan}

## 6. 내가 정리한 탐구 자료
{notes}

## 7. 결과 분석 방향
{shape['analysis']} 또한 결과를 해석할 때 단순히 '많다/적다'로 끝내지 말고, 왜 그런 응답이 나왔는지 생활 경험, 학교 환경, 자료조사 내용과 연결해 설명한다.

보고서에 넣으면 좋은 문장 틀:
- 설문 결과, 가장 많이 나타난 응답은 `___`였고, 이는 `___` 때문으로 해석할 수 있다.
- 자료조사에서 확인한 `___` 내용은 우리 반/학교 학생들의 응답과 `비슷했다/달랐다`.
- 예상과 달랐던 점은 `___`이며, 그 이유는 `___`일 가능성이 있다.

## 8. 결론
이번 탐구를 통해 `{topic}`은 학생들의 생활과 분리된 문제가 아니라, 실제 선택과 행동에 영향을 주는 주제임을 확인할 수 있었다. 특히 `___` 결과가 중요했으며, 이는 앞으로 학교생활에서 `___`을 고려해야 함을 보여준다.

## 9. 제안
{profile['proposal']}을 중심으로 다음과 같은 실천 방안을 제안할 수 있다.

1. 학생 개인: `___`을 실천한다.
2. 학급/학교: `___` 활동이나 규칙을 마련한다.
3. 추가 탐구: 이번 조사에서 부족했던 `___`을 더 확인한다.

## 10. 보완할 점
- 설문 참여 인원이 충분했는지 확인한다.
- 응답자가 한 학급이나 친한 친구에게 치우치지 않았는지 확인한다.
- 자료 출처의 작성자, 날짜, 기관을 기록한다.
- 결론이 자료와 설문 결과에서 실제로 나온 내용인지 다시 점검한다.
"""
