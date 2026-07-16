INTEREST_PROFILES = {
    "AI": ("인공지능 활용", "추천, 예측, 판단 보조, 윤리"),
    "스마트폰": ("스마트폰 사용", "생활 습관, 집중력, 디지털 안전"),
    "유튜브": ("영상 플랫폼 이용", "추천 알고리즘, 시청 습관, 정보 신뢰도"),
    "SNS": ("SNS 이용", "자기표현, 관계 형성, 정보 확산"),
    "게임": ("게임 활동", "몰입, 전략 선택, 협동 경험"),
    "웹툰": ("웹툰 콘텐츠", "서사 구조, 그림 표현, 독자 반응"),
    "K-POP": ("K-POP 팬 활동과 콘텐츠", "문화 확산, 팬덤 소통, 미디어 영향"),
    "영화": ("영화 감상과 장면 연출", "메시지 전달, 감정 변화, 사회 문제 표현"),
    "음악": ("음악 감상과 창작", "감정 변화, 집중, 표현 방식"),
    "스포츠": ("운동 경기와 훈련", "기록 향상, 자세 교정, 부상 예방"),
    "건강": ("건강한 생활 습관", "운동, 수면, 스트레스 관리"),
    "수면": ("수면 습관", "수면 시간, 집중력, 생활 리듬"),
    "스트레스": ("스트레스 관리", "원인, 해소 방법, 학교생활 영향"),
    "음식": ("음식 선택과 식생활", "건강, 소비 습관, 문화 차이"),
    "환경": ("환경 보호 실천", "자원 절약, 탄소 배출, 생활 속 변화"),
    "기후변화": ("기후변화 대응", "기온 변화, 재난, 생활 속 실천"),
    "플라스틱": ("플라스틱 사용", "일회용품, 미세플라스틱, 대체재"),
    "동물": ("동물 행동과 공존", "생명 존중, 돌봄, 환경 적응"),
    "생명윤리": ("생명과학 윤리", "유전자, 동물실험, 의료 판단"),
    "과학": ("과학 원리와 실험", "관찰, 변인 통제, 원리 적용"),
    "로봇": ("로봇 기술과 자동화", "센서 활용, 반복 작업, 인간 보조"),
    "데이터": ("데이터 분석", "수집 방법, 시각화, 해석 기준"),
    "수학": ("수학적 사고", "패턴, 모델링, 문제 해결"),
    "학습법": ("학습 전략", "복습 방법, 집중 환경, 자기주도성"),
    "독서": ("독서 활동", "이해도, 표현력, 관점 형성"),
    "진로": ("진로 탐색", "직업 이해, 역량 준비, 미래 변화"),
    "친구관계": ("친구 관계와 소통", "공감, 갈등 해결, 협력"),
    "학교생활": ("학교생활", "학습, 관계, 규칙, 공간 활용"),
    "소비습관": ("청소년 소비", "가격 비교, 충동구매, 가치소비"),
    "지역사회": ("지역사회 문제", "공공시설, 안전, 참여와 개선"),
    "여행": ("여행 경험과 지역 탐색", "문화 이해, 이동, 지역 문제"),
    "패션": ("패션과 자기표현", "소비 선택, 유행, 개성 표현"),
}

CUSTOM_INTEREST_KEYWORDS = [
    (["축구", "농구", "야구", "배구", "탁구", "배드민턴", "수영", "달리기", "태권도", "운동", "스포츠"], "스포츠"),
    (["게임", "로블록스", "마인크래프트", "브롤스타즈", "피파", "롤", "오버워치"], "게임"),
    (["유튜브", "영상", "쇼츠", "인플루언서"], "유튜브"),
    (["SNS", "인스타", "틱톡", "소셜미디어", "릴스"], "SNS"),
    (["웹툰", "만화"], "웹툰"),
    (["영화", "드라마", "애니"], "영화"),
    (["노래", "음악", "악기", "밴드", "랩", "댄스"], "음악"),
    (["아이돌", "케이팝", "KPOP", "K-POP"], "K-POP"),
    (["AI", "인공지능", "챗GPT", "챗지피티"], "AI"),
    (["로봇", "드론", "코딩", "프로그래밍"], "로봇"),
    (["환경", "기후", "분리수거", "플라스틱", "제로웨이스트"], "환경"),
    (["기후변화", "기후위기", "폭염", "탄소", "온실가스"], "기후변화"),
    (["플라스틱", "미세플라스틱", "일회용품", "재활용"], "플라스틱"),
    (["건강", "수면", "스트레스", "식습관", "다이어트"], "건강"),
    (["잠", "수면", "수면시간", "불면"], "수면"),
    (["스트레스", "불안", "긴장", "마음"], "스트레스"),
    (["생명윤리", "유전자", "동물실험", "의료윤리"], "생명윤리"),
    (["데이터", "통계", "그래프", "설문결과"], "데이터"),
    (["수학", "패턴", "모델링"], "수학"),
    (["학습법", "공부법", "복습", "암기", "집중"], "학습법"),
    (["독서", "책", "소설", "비문학"], "독서"),
    (["소비", "용돈", "충동구매", "가치소비"], "소비습관"),
    (["지역사회", "마을", "동네", "공공시설", "교통"], "지역사회"),
    (["친구", "우정", "관계", "소통"], "친구관계"),
    (["진로", "직업", "꿈"], "진로"),
    (["공부", "학습", "시험", "수업"], "학교생활"),
]

DOMAIN_PAIR_TEMPLATES = {
    ("스포츠", "스포츠"): [
        ("{first}와 {second} 참여 학생의 운동 동기와 지속 요인 비교", "체육", "중", "설문형", 3),
        ("{first}와 {second}에서 팀워크가 경기 만족도에 미치는 영향", "사회", "중", "설문형", 3),
        ("{first}와 {second}의 부상 예방 습관과 준비운동 실천 비교", "체육", "중", "자료조사형", 3),
        ("중·고등학생이 {first}와 {second} 중 하나를 선택할 때 중요하게 보는 기준 분석", "체육", "하", "설문형", 2),
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
        ("중·고등학생이 스포츠 영상을 보고 실제 운동을 따라 할 때 필요한 안전 기준 만들기", "체육", "중", "실천형", 3),
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
    ("{interest}에 대한 중·고등학생의 인식과 선호도 분석", "사회", "하", "설문형", 3),
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
    school += _keyword_score(topic, ["학교", "학급", "학생", "중학생", "고등학생", "중·고등학생", "캠페인", "생활", "실천", "수업", "동아리"], 3)

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
    return items[:15]


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
        "solution": "중·고등학생에게 현실적으로 맞는 건강 실천 방법",
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

MATH_SCIENCE_CONCEPTS = {
    "math": ["원주율", "방정식", "함수", "그래프", "확률", "통계", "기하", "도형", "피타고라스", "삼각함수", "로그", "수열", "미분", "적분", "벡터", "행렬"],
    "biology": ["혈액", "혈액형", "세포", "DNA", "유전자", "효소", "호르몬", "면역", "백혈구", "적혈구", "혈소판", "심장", "호흡", "광합성", "미생물"],
    "chemistry": ["원소", "분자", "화학", "산성", "염기성", "중화", "용액", "농도", "반응속도", "촉매", "이온", "전해질", "산화", "환원"],
    "physics": ["힘", "운동", "속도", "가속도", "에너지", "전기", "전류", "전압", "자기장", "빛", "파동", "소리", "열", "압력", "밀도"],
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
        "SNS": "정보",
        "스마트폰": "정보",
        "AI": "정보",
        "로봇": "기술",
        "데이터": "수학",
        "수학": "수학",
        "건강": "보건",
        "수면": "보건",
        "스트레스": "보건",
        "환경": "과학",
        "기후변화": "과학",
        "플라스틱": "과학",
        "동물": "과학",
        "생명윤리": "도덕",
        "친구관계": "도덕",
        "진로": "진로",
        "학습법": "진로",
        "독서": "국어",
        "웹툰": "국어",
        "영화": "국어",
        "음악": "음악",
        "K-POP": "사회",
        "패션": "사회",
        "음식": "보건",
        "학교생활": "사회",
        "소비습관": "사회",
        "지역사회": "사회",
        "여행": "사회",
    }.get(category, "사회")


def _pair_label(first: str, second: str) -> str:
    return f"{first}·{second}"


def _josa(word: str, with_batchim: str, without_batchim: str) -> str:
    if not word:
        return without_batchim
    code = ord(word[-1])
    if 0xAC00 <= code <= 0xD7A3:
        return with_batchim if (code - 0xAC00) % 28 else without_batchim
    return without_batchim


def _reason_for_single_topic(info: dict, topic: str, kind: str, index: int = 0) -> str:
    name = info["name"]
    domain = info["domain"]
    focus = info["focus"]
    variants = {
        "자료": [
            f"'{topic}' 주제는 {domain}을 막연한 주장으로 끝내지 않고 실제 사례, 통계, 관찰 자료로 확인하기 좋습니다.",
            f"{focus}와 관련된 자료를 모아 학생 생활 속 경향을 분석할 수 있어 '{name}' 관심사를 구체적인 탐구로 연결합니다.",
            f"학교나 생활 주변에서 찾을 수 있는 근거를 바탕으로 '{topic}'의 특징을 설명할 수 있습니다.",
        ],
        "개선": [
            f"'{topic}'은 {name} 관심을 학교에서 실천 가능한 해결 방법이나 캠페인으로 발전시킬 수 있는 주제입니다.",
            f"{focus}에서 생기는 불편함을 찾고, 학생이 직접 적용해 볼 개선안을 만들 수 있습니다.",
            f"자료조사와 설문 결과를 바탕으로 '{topic}'에 대한 현실적인 실천 방안을 제안할 수 있습니다.",
        ],
        "윤리": [
            f"'{topic}'은 {name}을 둘러싼 장점과 걱정, 공정성 기준을 함께 따져 볼 수 있는 주제입니다.",
            f"{focus}와 관련해 학생들이 어떤 기준으로 판단해야 하는지 찬반 근거를 비교하기 좋습니다.",
            f"단순 선호 조사가 아니라 '{topic}' 속 책임 있는 선택 기준을 세워 볼 수 있습니다.",
        ],
        "안전": [
            f"'{topic}'은 {domain}을 더 안전하고 바람직하게 이용하기 위한 기준을 학생 눈높이에서 만들 수 있는 주제입니다.",
            f"{focus}에서 생길 수 있는 위험 요인을 실제 사례와 설문으로 확인하기 좋습니다.",
            f"친구들이 바로 적용할 수 있는 약속이나 안내 기준까지 제안할 수 있습니다.",
        ],
        "비교": [
            f"'{topic}' 주제는 두 대상이나 조건을 같은 기준으로 비교해 {name}에 대한 막연한 생각을 근거로 바꿀 수 있습니다.",
            f"{focus}가 학생마다 어떻게 다르게 나타나는지 비교표와 설문 결과로 설명하기 좋습니다.",
            f"서로 다른 경험을 가진 학생들의 차이를 분석해 '{topic}'의 핵심 기준을 찾을 수 있습니다.",
        ],
        "선택": [
            f"'{topic}' 주제는 학생들이 {name}과 관련해 무엇을 중요하게 보는지 선택 기준을 직접 조사하기 좋습니다.",
            f"{focus} 중 어떤 요소가 실제 선택에 영향을 주는지 설문과 인터뷰로 확인할 수 있습니다.",
            f"친구들의 판단 기준을 모아 '{topic}'에 대한 우선순위와 이유를 분석할 수 있습니다.",
        ],
        "영향": [
            f"'{topic}' 주제는 {name}이 학생의 생활, 관계, 학습 태도에 어떤 변화를 만드는지 확인하기 좋습니다.",
            f"{focus}와 관련된 경험을 설문으로 모아 어떤 요인이 결과에 영향을 주는지 살필 수 있습니다.",
            f"자료조사와 친구들의 실제 경험을 연결해 '{topic}'의 원인과 결과를 설명할 수 있습니다.",
        ],
    }
    choices = variants.get(kind, variants["영향"])
    reason = choices[index % len(choices)]
    if topic not in reason:
        reason = f"{reason} 이 탐구의 핵심 질문은 '{topic}'입니다."
    return reason


def _concept_area(name: str) -> str:
    lowered = name.lower()
    for area, keywords in MATH_SCIENCE_CONCEPTS.items():
        if any(keyword.lower() in lowered for keyword in keywords):
            return area
    return ""


def _advanced_concept_topics(info: dict) -> list[dict]:
    n = info["name"]
    area = _concept_area(n)
    if area == "math":
        subject = "수학"
        reason = f"'{n}'의 정의, 증명, 역사, 활용 원리를 스스로 설명하고 탐구할 수 있도록 만든 심화 개념형 주제입니다."
        eun = _josa(n, "은", "는")
        eul = _josa(n, "을", "를")
        if "원주율" in n:
            return [
                _make_topic("원주율은 왜 3.14로 시작할까?", subject, "자료", 4, reason, 10),
                _make_topic("원주율이 무리수인 이유는 무엇일까?", subject, "자료", 5, reason, 10),
                _make_topic("원주율은 어떻게 끝없이 이어지는 수임을 알 수 있을까?", subject, "자료", 5, reason, 9),
                _make_topic("원주율을 직접 측정하면 왜 항상 오차가 생길까?", subject, "영향", 4, reason, 9),
                _make_topic("원주율을 계산하는 고대 방법과 현대 알고리즘은 어떻게 다를까?", subject, "비교", 5, reason, 9),
                _make_topic("원주율과 원의 넓이 공식은 어떻게 연결될까?", subject, "자료", 4, reason, 8),
                _make_topic("아르키메데스는 원주율을 어떻게 추정했을까?", subject, "자료", 4, reason, 8),
                _make_topic("원주율의 소수점 숫자에는 규칙이 있을까?", subject, "자료", 4, reason, 8),
                _make_topic("원주율을 3.14 대신 22/7로 쓰면 어떤 차이가 생길까?", subject, "비교", 4, reason, 7),
                _make_topic("원주율은 원이 아닌 곳에서도 왜 나타날까?", subject, "자료", 5, reason, 7),
                _make_topic("원주율과 삼각함수는 어떤 관계가 있을까?", subject, "자료", 5, reason, 7),
                _make_topic("컴퓨터는 원주율을 어떻게 빠르게 계산할까?", "정보", "개선", 5, reason, 7),
                _make_topic("원주율 암기는 수학적 이해에 실제로 도움이 될까?", subject, "비교", 3, reason, 6),
                _make_topic("원주율 근삿값의 자리 수가 늘어나면 실제 계산 결과는 얼마나 달라질까?", subject, "자료", 4, reason, 6),
                _make_topic("원주율을 설명하는 여러 비유는 어디까지 정확할까?", "국어", "비교", 3, reason, 6),
            ]
        return [
            _make_topic(f"{n}{eun} 왜 필요한 수학 개념일까?", subject, "자료", 4, reason, 10),
            _make_topic(f"{n}의 정의는 어떻게 만들어졌을까?", subject, "자료", 4, reason, 9),
            _make_topic(f"{n}{eun} 어떤 조건에서 성립하고 어떤 조건에서 달라질까?", subject, "자료", 5, reason, 9),
            _make_topic(f"{n}{eul} 그림, 표, 식으로 표현하면 무엇이 달라질까?", subject, "비교", 4, reason, 9),
            _make_topic(f"{n}{eul} 잘못 이해할 때 생기는 대표적인 오개념은 무엇일까?", subject, "비교", 4, reason, 8),
            _make_topic(f"{n}{eul} 증명하거나 설명하는 여러 방법은 어떻게 다를까?", subject, "비교", 5, reason, 8),
            _make_topic(f"{n}{eun} 실제 문제를 모델링할 때 어떤 역할을 할까?", subject, "자료", 5, reason, 8),
            _make_topic(f"{n} 문제에서 풀이 전략에 따라 사고 과정은 어떻게 달라질까?", subject, "비교", 4, reason, 7),
            _make_topic(f"{n}{eul} 컴퓨터 시뮬레이션으로 표현할 수 있을까?", "정보", "개선", 5, reason, 7),
            _make_topic(f"{n}{eun} 과학이나 공학 문제 해결에 어떻게 쓰일까?", "과학", "자료", 4, reason, 7),
            _make_topic(f"{n}의 역사적 발견 과정은 오늘날의 수학 학습과 어떻게 연결될까?", subject, "자료", 4, reason, 6),
            _make_topic(f"{n}{eul} 설명하는 가장 정확한 비유는 무엇일까?", "국어", "비교", 3, reason, 6),
            _make_topic(f"{n}{eul} 활용한 탐구형 문항은 어떻게 만들 수 있을까?", subject, "개선", 4, reason, 6),
            _make_topic(f"{n}{eul} 이해했다는 것은 무엇을 할 수 있다는 뜻일까?", subject, "자료", 3, reason, 5),
            _make_topic(f"{n}{eul} 중·고등학생 수준에서 더 깊게 탐구하려면 어떤 질문이 필요할까?", subject, "자료", 3, reason, 5),
        ]
    if area == "biology":
        subject = "생명과학"
        reason = f"'{n}'의 구조, 기능, 조절 원리, 건강과의 관계를 깊게 설명하도록 만든 심화 생명과학 주제입니다."
        eun = _josa(n, "은", "는")
        eul = _josa(n, "을", "를")
        gwa = _josa(n, "과", "와")
        return [
            _make_topic(f"{n}{eun} 몸속에서 정확히 어떤 역할을 할까?", subject, "자료", 4, reason, 10),
            _make_topic(f"{n}의 구조와 기능은 어떻게 연결될까?", subject, "자료", 5, reason, 10),
            _make_topic(f"{n}{_josa(n, '이', '가')} 항상성 유지에 중요한 이유는 무엇일까?", subject, "자료", 5, reason, 9),
            _make_topic(f"{n}에 이상이 생기면 몸에서는 어떤 변화가 나타날까?", "보건", "영향", 4, reason, 9),
            _make_topic(f"{n} 검사 결과는 어떤 생명과학 개념으로 해석할 수 있을까?", subject, "자료", 5, reason, 8),
            _make_topic(f"{n}{gwa} 면역 반응은 어떻게 연결될까?", subject, "자료", 4, reason, 8),
            _make_topic(f"{n}{eun} 운동, 수면, 식습관과 어떤 관계가 있을까?", "보건", "영향", 4, reason, 8),
            _make_topic(f"{n}에 대한 흔한 오개념은 왜 생길까?", subject, "비교", 3, reason, 7),
            _make_topic(f"{n}{eul} 모형으로 설명하면 어떤 한계가 있을까?", subject, "비교", 4, reason, 7),
            _make_topic(f"{n} 관련 질병은 어떤 원리로 발생하고 예방할 수 있을까?", "보건", "자료", 4, reason, 7),
            _make_topic(f"{n} 관련 의학 정보는 어떻게 신뢰도를 판단해야 할까?", subject, "윤리", 4, reason, 6),
            _make_topic(f"{n}을 관찰하거나 실험할 때 어떤 변인을 통제해야 할까?", subject, "안전", 4, reason, 6),
            _make_topic(f"{n} 변화는 다른 기관계와 어떻게 연결될까?", subject, "자료", 4, reason, 6),
            _make_topic(f"{n}을 설명하는 좋은 질문과 나쁜 질문은 어떻게 다를까?", "국어", "비교", 3, reason, 5),
            _make_topic(f"{n}을 중·고등학생 수준에서 깊게 탐구하려면 어떤 자료가 필요할까?", subject, "자료", 3, reason, 5),
        ]
    if area == "chemistry":
        subject = "화학"
        reason = f"'{n}'의 입자 수준 원리, 반응 조건, 실험 설계와 생활 속 물질을 연결한 심화 화학 주제입니다."
        eun = _josa(n, "은", "는")
        eul = _josa(n, "을", "를")
        return [
            _make_topic(f"{n}{eun} 입자 수준에서 어떤 일이 일어나는 현상일까?", subject, "자료", 5, reason, 10),
            _make_topic(f"{n} 반응은 왜 특정 조건에서 더 잘 일어날까?", subject, "영향", 5, reason, 10),
            _make_topic(f"{n}{eul} 설명할 때 원자, 분자, 이온 개념은 어떻게 쓰일까?", subject, "자료", 4, reason, 9),
            _make_topic(f"{n} 실험에서 농도와 온도는 결과를 어떻게 바꿀까?", subject, "영향", 5, reason, 9),
            _make_topic(f"{n} 반응의 속도를 결정하는 요인은 무엇일까?", subject, "영향", 4, reason, 8),
            _make_topic(f"{n}{eul} 눈에 보이는 모형으로 표현하면 무엇을 놓치게 될까?", subject, "비교", 4, reason, 8),
            _make_topic(f"{n} 실험에서 변인을 통제하지 않으면 왜 결론이 흔들릴까?", subject, "안전", 4, reason, 8),
            _make_topic(f"{n}과 생활용품의 성분 표시는 어떻게 연결될까?", subject, "윤리", 4, reason, 7),
            _make_topic(f"{n} 관련 오개념은 왜 생기고 어떻게 바로잡을 수 있을까?", subject, "비교", 3, reason, 7),
            _make_topic(f"{n}{eun} 환경 문제 해결에 실제로 도움이 될까?", "과학", "개선", 4, reason, 7),
            _make_topic(f"{n} 실험의 오차는 어디에서 발생할까?", subject, "자료", 4, reason, 6),
            _make_topic(f"{n} 관련 뉴스 속 과학 표현은 얼마나 정확할까?", "국어", "윤리", 3, reason, 6),
            _make_topic(f"{n}{eun} 의약품, 식품, 환경 분야에서 왜 중요할까?", subject, "자료", 4, reason, 6),
            _make_topic(f"{n}{eul} 학교에서 안전하게 탐구하려면 어떤 실험 설계가 필요할까?", subject, "개선", 4, reason, 5),
            _make_topic(f"{n}{eul} 중·고등학생 수준에서 깊게 탐구하려면 어떤 질문이 좋을까?", subject, "자료", 3, reason, 5),
        ]
    if area == "physics":
        subject = "물리"
        reason = f"'{n}'의 법칙, 측정, 변인 통제, 모델링을 중심으로 현상을 설명하도록 만든 심화 물리 주제입니다."
        eun = _josa(n, "은", "는")
        eul = _josa(n, "을", "를")
        gwa = _josa(n, "과", "와")
        return [
            _make_topic(f"{n}{eun} 왜 물체의 상태를 바꾸는 원인이 될까?", subject, "자료", 4, reason, 10),
            _make_topic(f"{n}{eul} 정확히 측정하려면 어떤 조건이 필요할까?", subject, "자료", 5, reason, 10),
            _make_topic(f"{n}{gwa} 에너지 전환은 어떻게 연결될까?", subject, "자료", 5, reason, 9),
            _make_topic(f"{n} 실험에서 변인을 통제하지 않으면 왜 결론이 달라질까?", subject, "영향", 4, reason, 9),
            _make_topic(f"{n}{eul} 그래프로 나타내면 어떤 법칙을 발견할 수 있을까?", subject, "자료", 5, reason, 8),
            _make_topic(f"{n} 개념을 시뮬레이션으로 표현하면 무엇을 설명할 수 있을까?", "정보", "개선", 5, reason, 8),
            _make_topic(f"{n}에 대한 학생 오개념은 왜 생길까?", subject, "비교", 3, reason, 8),
            _make_topic(f"{n} 변화는 운동 상태를 어떻게 바꿀까?", subject, "영향", 4, reason, 7),
            _make_topic(f"{n}과 안전 기준은 어떤 물리 원리로 연결될까?", subject, "안전", 4, reason, 7),
            _make_topic(f"{n}{eul} 활용한 측정 장치는 어떻게 설계할 수 있을까?", "기술", "개선", 4, reason, 7),
            _make_topic(f"{n} 관련 생활 속 현상은 어떤 법칙으로 설명될까?", subject, "자료", 4, reason, 6),
            _make_topic(f"{n} 실험 결과의 오차는 어디에서 생길까?", subject, "자료", 4, reason, 6),
            _make_topic(f"{n}{eun} 공학적 문제 해결에 어떻게 활용될까?", "기술", "자료", 4, reason, 6),
            _make_topic(f"{n}{eul} 시각화한 자료는 어디까지 정확할까?", subject, "비교", 3, reason, 5),
            _make_topic(f"{n}{eul} 중·고등학생 수준에서 깊게 탐구하려면 어떤 질문이 필요할까?", subject, "자료", 3, reason, 5),
        ]
    return []


CURATED_SINGLE_TOPICS = {
    "AI": [("생성형 AI를 사용한 과제와 직접 작성한 과제는 어떤 차이가 있을까?", "정보", "비교", 4), ("AI 추천 결과에는 어떤 편향이 숨어 있을까?", "정보", "윤리", 4), ("학생들은 AI 답변의 신뢰도를 어떻게 판단해야 할까?", "정보", "윤리", 4)],
    "스마트폰": [("스마트폰 알림은 집중 시간에 어떤 영향을 줄까?", "정보", "영향", 4), ("취침 전 스마트폰 사용은 수면의 질과 어떤 관련이 있을까?", "보건", "영향", 4), ("스마트폰 사용 시간을 줄이는 방법은 실제로 효과가 있을까?", "보건", "개선", 4)],
    "유튜브": [("유튜브 추천 알고리즘은 시청 습관을 어떻게 바꿀까?", "정보", "자료", 4), ("쇼츠 시청 시간은 집중력과 학습 태도에 어떤 영향을 줄까?", "정보", "영향", 4), ("유튜브 정보의 신뢰도를 판단하는 학생 기준은 무엇일까?", "정보", "윤리", 4)],
    "SNS": [("SNS 사용은 자존감과 친구 관계에 어떤 영향을 줄까?", "도덕", "영향", 4), ("SNS에서 정보가 빠르게 퍼지는 이유는 무엇일까?", "정보", "자료", 4), ("SNS 비교 문화는 청소년의 소비와 자기표현에 어떤 영향을 줄까?", "사회", "영향", 4)],
    "게임": [("게임의 보상 구조는 몰입과 자기조절에 어떤 영향을 줄까?", "정보", "영향", 4), ("협동 게임 경험은 실제 친구 관계와 의사소통에 도움이 될까?", "도덕", "영향", 4), ("확률형 아이템은 청소년 소비 판단에 어떤 영향을 줄까?", "사회", "윤리", 4)],
    "웹툰": [("웹툰의 댓글 문화는 작품 해석에 어떤 영향을 줄까?", "국어", "영향", 4), ("웹툰 속 갈등 구조는 청소년의 공감 형성에 어떤 도움을 줄까?", "국어", "자료", 4), ("웹툰 원작 영상화는 독자의 기대와 만족도를 어떻게 바꿀까?", "국어", "비교", 4)],
    "K-POP": [("K-POP 팬덤 활동은 문화 확산에 어떤 역할을 할까?", "사회", "자료", 4), ("아이돌 콘텐츠 소비는 청소년의 시간 관리에 어떤 영향을 줄까?", "사회", "영향", 4), ("K-POP 굿즈 소비는 가치소비와 충동구매 중 어디에 가까울까?", "사회", "윤리", 4)],
    "영화": [("영화 속 사회 문제 표현은 관객의 인식 변화에 영향을 줄까?", "국어", "영향", 4), ("같은 사건을 다룬 영화와 뉴스는 관점을 어떻게 다르게 보여줄까?", "국어", "비교", 4), ("영화 장면의 음악과 색감은 감정 이해에 어떤 영향을 줄까?", "국어", "자료", 4)],
    "음악": [("음악 감상은 스트레스와 집중 상태에 어떤 영향을 줄까?", "음악", "영향", 4), ("공부할 때 듣는 음악은 학습 효율을 높일까 낮출까?", "음악", "비교", 4), ("가사 내용은 청소년의 감정 표현에 어떤 도움을 줄까?", "음악", "자료", 4)],
    "스포츠": [("준비운동은 부상 예방에 실제로 얼마나 도움이 될까?", "체육", "자료", 4), ("운동 기록을 향상시키는 요인은 자세, 훈련량, 휴식 중 무엇일까?", "체육", "비교", 4), ("팀 스포츠 경험은 협동 태도와 책임감에 어떤 영향을 줄까?", "체육", "영향", 4)],
    "건강": [("청소년의 건강 습관에서 수면, 운동, 식습관 중 무엇이 가장 중요할까?", "보건", "비교", 4), ("건강 정보는 어디까지 믿고 따라야 할까?", "보건", "윤리", 4), ("학교생활 속 작은 건강 실천은 실제 변화를 만들 수 있을까?", "보건", "개선", 4)],
    "수면": [("수면 시간이 집중력과 기분 변화에 어떤 영향을 줄까?", "보건", "영향", 4), ("주말 늦잠은 부족한 수면을 보충할 수 있을까?", "보건", "자료", 4), ("취침 전 습관을 바꾸면 아침 피로감은 달라질까?", "보건", "개선", 4)],
    "스트레스": [("학생들이 스트레스를 가장 크게 느끼는 상황은 무엇일까?", "보건", "자료", 4), ("스트레스 해소 방법은 사람마다 왜 다르게 효과가 나타날까?", "보건", "비교", 4), ("학교에서 실천 가능한 스트레스 완화 방법은 무엇일까?", "보건", "개선", 4)],
    "음식": [("아침 식사는 수업 집중도에 어떤 영향을 줄까?", "보건", "영향", 4), ("배달 음식 이용은 청소년의 식습관과 소비 습관을 어떻게 바꿀까?", "보건", "영향", 4), ("식품 광고는 학생들의 음식 선택에 어떤 영향을 줄까?", "보건", "윤리", 4)],
    "환경": [("학교에서 가장 줄이기 쉬운 환경 문제는 무엇일까?", "과학", "자료", 4), ("환경 캠페인은 학생 행동을 실제로 바꿀 수 있을까?", "과학", "개선", 4), ("친환경 제품은 항상 환경에 더 좋다고 말할 수 있을까?", "과학", "윤리", 4)],
    "기후변화": [("기후변화는 우리 지역의 생활에 어떤 변화를 만들고 있을까?", "과학", "자료", 4), ("폭염과 집중호우에 학교는 어떻게 대응해야 할까?", "과학", "개선", 4), ("청소년의 작은 탄소 줄이기 실천은 어떤 의미가 있을까?", "과학", "자료", 4)],
    "플라스틱": [("일회용 플라스틱을 줄이기 어려운 이유는 무엇일까?", "과학", "자료", 4), ("미세플라스틱은 왜 생태계와 건강 문제로 이어질까?", "과학", "자료", 4), ("학교에서 플라스틱 사용을 줄이는 가장 현실적인 방법은 무엇일까?", "과학", "개선", 4)],
    "동물": [("반려동물 돌봄 경험은 생명 존중 태도에 영향을 줄까?", "과학", "영향", 4), ("동물 행동을 관찰하면 환경 적응 방식을 어떻게 알 수 있을까?", "과학", "자료", 4), ("동물 보호와 인간 편의가 충돌할 때 어떤 기준이 필요할까?", "도덕", "윤리", 4)],
    "생명윤리": [("동물실험은 어떤 조건에서 정당화될 수 있을까?", "도덕", "윤리", 4), ("유전자 검사 정보는 개인에게 어떤 도움과 위험을 줄까?", "도덕", "윤리", 4), ("의료 기술 발전에서 생명 존중 기준은 어떻게 세워야 할까?", "도덕", "자료", 4)],
    "과학": [("좋은 과학 실험에는 왜 변인 통제가 필요할까?", "과학", "자료", 4), ("생활 속 현상을 과학적으로 설명하려면 어떤 증거가 필요할까?", "과학", "자료", 4), ("과학 뉴스의 과장된 표현은 어떻게 구별할 수 있을까?", "과학", "윤리", 4)],
    "로봇": [("로봇은 사람의 일을 어디까지 대신할 수 있을까?", "기술", "자료", 4), ("센서 로봇은 주변 환경을 어떻게 판단할까?", "기술", "자료", 4), ("돌봄 로봇을 사용할 때 필요한 윤리 기준은 무엇일까?", "기술", "윤리", 4)],
    "데이터": [("같은 설문 결과도 그래프 표현에 따라 해석이 달라질까?", "수학", "비교", 4), ("평균만 보면 놓치게 되는 데이터의 특징은 무엇일까?", "수학", "자료", 4), ("학생 생활 데이터를 수집할 때 개인정보는 어떻게 보호해야 할까?", "수학", "윤리", 4)],
    "수학": [("수학은 실제 생활 문제를 어떻게 모델링할 수 있을까?", "수학", "자료", 4), ("문제 풀이 과정에서 다양한 전략은 왜 필요할까?", "수학", "비교", 4), ("수학 개념을 그림으로 표현하면 이해가 쉬워질까?", "수학", "비교", 4)],
    "학습법": [("반복 학습과 이해 중심 학습은 어떤 차이가 있을까?", "진로", "비교", 4), ("공부 장소와 집중 시간은 학습 효율에 어떤 영향을 줄까?", "진로", "영향", 4), ("자기주도학습을 지속하게 만드는 조건은 무엇일까?", "진로", "자료", 4)],
    "독서": [("독서량은 글쓰기 표현력과 어떤 관련이 있을까?", "국어", "영향", 4), ("종이책과 전자책은 이해도와 몰입감에 어떤 차이를 만들까?", "국어", "비교", 4), ("같은 책을 읽어도 학생마다 해석이 달라지는 이유는 무엇일까?", "국어", "자료", 4)],
    "진로": [("학생들은 진로를 선택할 때 어떤 정보를 가장 신뢰할까?", "진로", "자료", 4), ("AI 시대에 중요해지는 직업 역량은 무엇일까?", "진로", "자료", 4), ("진로 체험 활동은 실제 진로 결정에 도움을 줄까?", "진로", "영향", 4)],
    "친구관계": [("친구 사이 갈등은 어떤 소통 방식으로 줄일 수 있을까?", "도덕", "개선", 4), ("온라인 대화와 직접 대화는 관계 형성에 어떤 차이가 있을까?", "도덕", "비교", 4), ("공감 능력은 학급 분위기에 어떤 영향을 줄까?", "도덕", "영향", 4)],
    "학교생활": [("학생들이 학교생활에서 가장 개선하고 싶은 것은 무엇일까?", "사회", "자료", 4), ("학교 공간 배치는 휴식과 학습 만족도에 어떤 영향을 줄까?", "사회", "영향", 4), ("학급 규칙을 학생이 함께 만들면 실천율이 높아질까?", "사회", "개선", 4)],
    "소비습관": [("용돈 사용 기록은 소비 습관을 바꾸는 데 도움이 될까?", "사회", "자료", 4), ("청소년의 충동구매를 줄이는 방법은 무엇일까?", "사회", "개선", 4), ("가격, 브랜드, 후기 중 소비 선택에 가장 큰 영향을 주는 것은 무엇일까?", "사회", "비교", 4)],
    "지역사회": [("우리 지역에서 학생들이 가장 불편하게 느끼는 문제는 무엇일까?", "사회", "자료", 4), ("청소년이 지역사회 문제 해결에 참여할 수 있는 방법은 무엇일까?", "사회", "개선", 4), ("지역 공공시설은 학생들의 생활 만족도에 어떤 영향을 줄까?", "사회", "영향", 4)],
    "여행": [("여행 경험은 문화 이해와 지역 인식에 어떤 영향을 줄까?", "사회", "영향", 4), ("학생들은 여행지를 선택할 때 비용, 거리, 경험 중 무엇을 중요하게 볼까?", "사회", "비교", 4), ("지역 여행은 지역사회 이해에 도움이 될까?", "사회", "자료", 4)],
    "패션": [("패션은 자기표현과 또래 관계에 어떤 영향을 줄까?", "사회", "영향", 4), ("유행을 따르는 소비와 개성 표현은 어떻게 균형을 이룰 수 있을까?", "사회", "윤리", 4), ("패스트패션은 환경과 소비 습관에 어떤 문제를 만들까?", "사회", "자료", 4)],
}


def _curated_single_topics(info: dict) -> list[dict]:
    return [
        _make_topic(title, subject, kind, weeks, _reason_for_single_topic(info, title, kind, index), 24 - index)
        for index, (title, subject, kind, weeks) in enumerate(CURATED_SINGLE_TOPICS.get(info["category"], []))
    ]


def _single_interest_topics(info: dict) -> list[dict]:
    advanced = _advanced_concept_topics(info)
    if advanced:
        return advanced
    curated = _curated_single_topics(info)
    n = info["name"]
    d = info["domain"]
    f = info["focus"]
    subject = _subject_for(info)
    reason = ""
    generic = [
        _make_topic(f"학생들이 {n}에 관심을 갖는 이유는 무엇일까?", subject, "자료", 4, reason, 10),
        _make_topic(f"{n}{_josa(n, '과', '와')} 관련해 학생들이 가장 중요하게 생각하는 기준은 무엇일까?", "사회", "선택", 3, reason, 10),
        _make_topic(f"{d}에서 중요한 요소는 만족도에 어떤 차이를 만들까?", subject, "영향", 4, reason, 9),
        _make_topic(f"{n}에 관심이 높은 학생과 낮은 학생은 생활 습관이 어떻게 다를까?", "사회", "비교", 4, reason, 8),
        _make_topic(f"{n}에 대한 온라인 정보는 얼마나 믿을 수 있을까?", "정보", "윤리", 4, reason, 8),
        _make_topic(f"{n}과 관련한 활동이나 선택을 더 바람직하게 하려면 어떤 기준이 필요할까?", "도덕", "안전", 3, reason, 8),
        _make_topic(f"{n} 관심은 친구 관계나 소통 방식에 어떤 영향을 줄까?", "도덕", "영향", 3, reason, 7),
        _make_topic(f"{n}을 학교 수업이나 동아리 활동에 활용할 수 있을까?", "진로", "개선", 4, reason, 7),
        _make_topic(f"{n} 관련 뉴스와 영상은 같은 주제를 어떻게 다르게 보여줄까?", "국어", "비교", 4, reason, 7),
        _make_topic(f"{n}에 대한 학생 설문 결과와 실제 자료는 얼마나 비슷할까?", "수학", "자료", 4, reason, 6),
        _make_topic(f"{n} 관심은 진로 탐색에 어떤 도움을 줄 수 있을까?", "진로", "영향", 3, reason, 6),
        _make_topic(f"{n}과 관련해 학교에서 바꿀 수 있는 작은 문제는 무엇일까?", "사회", "개선", 4, reason, 6),
        _make_topic(f"{n}을 둘러싼 공정성, 접근성, 안전 문제는 무엇일까?", "도덕", "윤리", 4, reason, 5),
        _make_topic(f"{n}에 대해 친구들은 어떤 경험과 고민을 가지고 있을까?", "국어", "비교", 3, reason, 5),
        _make_topic(f"{n}을 더 깊이 탐구하려면 어떤 자료와 질문이 필요할까?", subject, "자료", 3, reason, 5),
    ]
    for index, item in enumerate(generic, start=len(curated)):
        item["reason"] = _reason_for_single_topic(info, item["topic"], _topic_kind(item["topic"]), index)
    return curated + generic


def _individual_mix_topics(a: dict, b: dict) -> list[dict]:
    first_topics = _single_interest_topics(a)
    second_topics = _single_interest_topics(b)
    mixed = []
    for left, right in zip(first_topics, second_topics):
        mixed.append(left)
        mixed.append(right)
    mixed.extend(first_topics[len(second_topics):])
    mixed.extend(second_topics[len(first_topics):])
    return mixed[:15]


def _travel_food_topics(first: str, second: str) -> list[dict]:
    pair = _pair_label(first, second)
    reason = f"'{first}'와 '{second}'를 억지로 붙이지 않고, 여행지 선택, 지역 음식, 식비, 위생, 문화 경험처럼 실제 조사 가능한 장면으로 바꾼 주제입니다."
    return [
        _make_topic("여행지의 지역 음식이 여행 만족도에 미치는 영향", "사회", "영향", 4, reason, 10),
        _make_topic("중·고등학생이 여행지를 고를 때 음식 정보는 얼마나 중요할까?", "사회", "선택", 3, reason, 9),
        _make_topic("SNS 맛집 정보는 여행 계획에 어떤 영향을 줄까?", "정보", "윤리", 4, reason, 9),
        _make_topic("지역 대표 음식은 그 지역의 문화와 역사를 어떻게 보여줄까?", "사회", "자료", 4, reason, 9),
        _make_topic("여행 중 식비 계획이 전체 여행 만족도에 미치는 영향", "수학", "자료", 4, reason, 8),
        _make_topic("여행지 음식 선택에서 가격, 위생, 맛, 거리 중 무엇이 가장 중요할까?", "사회", "비교", 3, reason, 8),
        _make_topic("지역 음식 체험이 여행지 기억에 오래 남는 이유는 무엇일까?", "국어", "비교", 3, reason, 8),
        _make_topic("관광지 음식 가격은 지역 주민과 관광객에게 어떻게 다르게 받아들여질까?", "사회", "비교", 4, reason, 7),
        _make_topic("여행지 음식 리뷰의 신뢰도를 판단하는 기준은 무엇일까?", "정보", "윤리", 4, reason, 7),
        _make_topic("로컬푸드 소비가 지역 경제와 환경에 주는 영향", "사회", "영향", 4, reason, 7),
        _make_topic("여행 중 음식 위생 정보를 학생들이 쉽게 확인하는 방법 제안", "보건", "안전", 3, reason, 6),
        _make_topic("학교 주변 지역 음식을 활용한 작은 여행 코스 설계", "진로", "개선", 3, reason, 6),
        _make_topic("여행지 음식 사진은 실제 선택과 기대감에 어떤 영향을 줄까?", "미술", "영향", 3, reason, 6),
        _make_topic("지역 축제의 음식 부스는 관광객 참여를 어떻게 높일까?", "사회", "자료", 4, reason, 5),
        _make_topic(f"{pair} 주제를 탐구할 때 설문과 자료조사를 어떻게 연결할까?", "사회", "자료", 3, reason, 5),
    ]


def _fusion_interest_topics(a: dict, b: dict) -> list[dict]:
    first = a["name"]
    second = b["name"]
    pair = _pair_label(first, second)
    a_cat = a["category"]
    b_cat = b["category"]
    reason = f"'{first}'와 '{second}'를 단순히 나열하지 않고, 학생 생활에서 두 관심사가 만나는 지점을 탐구 문제로 바꾼 주제입니다."
    topics = []
    a_area = _concept_area(first)
    b_area = _concept_area(second)

    if a_area or b_area:
        concept = first if a_area else second
        other = second if a_area else first
        concept_subject = {
            "math": "수학",
            "biology": "생명과학",
            "chemistry": "화학",
            "physics": "물리",
        }.get(a_area or b_area, "과학")
        reason = f"'{concept}' 개념을 '{other}' 관심사와 연결해 중·고등학생 수준의 융합 탐구 문제로 바꾼 주제입니다."
        topics.extend([
            _make_topic(f"{concept} 개념을 활용해 {other} 현상이나 사례를 설명하기", concept_subject, "자료", 4, reason, 10),
            _make_topic(f"{concept}과 {other}를 연결한 실제 데이터 수집 및 분석 탐구", concept_subject, "자료", 5, reason, 10),
            _make_topic(f"{concept} 원리를 {other} 활동에 적용할 때 생기는 장점과 한계 분석", concept_subject, "영향", 4, reason, 9),
            _make_topic(f"{concept} 개념을 {other} 주제로 설명하는 시각화 자료 제작과 효과 비교", concept_subject, "비교", 4, reason, 9),
            _make_topic(f"{concept} 관련 오개념이 {other} 이해에 미치는 영향", concept_subject, "영향", 4, reason, 8),
            _make_topic(f"{concept}과 {other}를 융합한 탐구형 실험 또는 관찰 계획 설계", concept_subject, "개선", 5, reason, 8),
            _make_topic(f"{concept} 관련 자료와 {other} 사례의 신뢰도 비교 분석", concept_subject, "윤리", 4, reason, 8),
            _make_topic(f"{concept}을 바탕으로 {other} 문제를 모델링하는 방법 탐구", concept_subject, "자료", 5, reason, 7),
            _make_topic(f"{concept}과 {other}의 관계를 설명하는 수업용 탐구 활동 설계", "진로", "개선", 4, reason, 7),
            _make_topic(f"{concept} 개념을 활용한 {other} 관련 진로와 기술 활용 사례 조사", "진로", "자료", 4, reason, 7),
            _make_topic(f"{concept}과 {other}를 주제로 한 학생 설문과 자료조사 결과 비교", "사회", "비교", 3, reason, 6),
            _make_topic(f"{concept} 관련 실험 안전 기준을 {other} 활동과 연결해 제안하기", concept_subject, "안전", 4, reason, 6),
            _make_topic(f"{concept}의 역사적 발전과 {other} 분야 활용 사례 분석", concept_subject, "자료", 4, reason, 6),
            _make_topic(f"{concept}을 {other}와 연결해 중·고등학생 탐구 보고서 주제로 발전시키는 방법", concept_subject, "개선", 3, reason, 5),
            _make_topic(f"{concept}과 {other} 융합 주제에서 추가로 탐구할 변인과 측정 방법 분석", concept_subject, "자료", 4, reason, 5),
        ])
        return topics

    if {a_cat, b_cat} == {"여행", "음식"}:
        return _travel_food_topics(first, second)

    if a_cat == b_cat:
        subject = _subject_for(a)
        topics.extend([
            _make_topic(f"{pair} 선택 기준을 행동, 환경, 비용, 접근성 변인으로 비교 분석", subject, "비교", 4, reason, 10),
            _make_topic(f"{pair} 참여 경험이 관계 형성, 자기관리, 학교생활 만족도에 미치는 영향", "사회", "영향", 4, reason, 9),
            _make_topic(f"{pair} 활동을 더 안전하고 지속적으로 운영하기 위한 근거 기반 기준 만들기", subject, "안전", 4, reason, 9),
            _make_topic(f"{pair} 관련 자료와 학생 설문 결과가 다르게 나타나는 이유 분석", "수학", "자료", 4, reason, 8),
            _make_topic(f"{pair} 분야의 공정성, 접근성, 참여 격차 문제와 개선 방안 탐구", "도덕", "윤리", 4, reason, 8),
        ])
        return topics

    return _individual_mix_topics(a, b)


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
    return ranked[:15]


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


GUIDE_PROFILES = [
    {
        "keywords": ["AI", "인공지능", "알고리즘", "추천", "로봇", "센서", "자동화", "스마트폰", "앱"],
        "source": "기술 원리 설명, 실제 서비스 화면, 오류·편향 사례, 개인정보 보호 기준",
        "field": "같은 기능을 쓰는 학생과 쓰지 않는 학생의 사용 경험을 나누어 기록",
        "survey": "사용 빈도, 편리함, 불안감, 신뢰도, 개인정보 걱정",
        "target": "자주 사용하는 학생, 거의 사용하지 않는 학생, 정보 교사 또는 기기 담당자",
        "interview": "기술을 믿거나 의심하게 된 실제 장면과 그 이유",
        "analysis": "편리함과 위험을 따로 점수화하고, 경험 유무에 따른 응답 차이를 비교",
        "product": "학생용 안전 사용 기준 또는 기능 개선 체크리스트",
    },
    {
        "keywords": ["스포츠", "운동", "축구", "농구", "야구", "배구", "훈련", "경기", "자세", "부상", "기록"],
        "source": "훈련 방법 자료, 부상 예방 자료, 경기 기록, 학교 체육 활동 사례",
        "field": "준비운동, 참여 시간, 장비, 휴식처럼 관찰 가능한 장면을 체크리스트로 기록",
        "survey": "참여 동기, 흥미 유지 요인, 부상 경험, 안전 수칙 실천 정도",
        "target": "해당 활동 경험자, 초보자, 체육 교사 또는 운동부 학생",
        "interview": "기록 향상이나 안전에 실제로 도움이 된 습관",
        "analysis": "경험 수준별로 응답을 나누고, 부상 예방 습관과 만족도의 관계를 비교",
        "product": "학교 체육 시간에 적용할 수 있는 안전·참여 기준",
    },
    {
        "keywords": ["유튜브", "영상", "미디어", "SNS", "틱톡", "릴스", "콘텐츠", "웹툰", "영화", "K-POP", "음악"],
        "source": "콘텐츠 사례, 댓글·추천 화면 관찰, 청소년 미디어 이용 통계, 관련 뉴스",
        "field": "콘텐츠 유형, 시청 시간대, 추천 방식, 댓글 분위기를 표본으로 정해 관찰",
        "survey": "이용 목적, 시청 시간, 감정 변화, 정보 신뢰도, 친구와 공유 여부",
        "target": "많이 이용하는 학생, 적게 이용하는 학생, 콘텐츠를 만들어 본 학생",
        "interview": "계속 보게 만드는 요소와 이용 후 생활에 생긴 변화",
        "analysis": "이용 목적별 응답을 묶고, 긍정 효과와 부정 영향을 균형 있게 비교",
        "product": "건강한 미디어 이용 약속 또는 콘텐츠 판별 기준",
    },
    {
        "keywords": ["환경", "기후", "탄소", "분리수거", "플라스틱", "재활용", "쓰레기", "에너지", "동물", "생태"],
        "source": "학교 주변 관찰 기록, 공공기관 환경 자료, 캠페인 사례, 제품 표시 정보",
        "field": "교실·급식실·복도 등 장소별 쓰레기, 전기 사용, 실천 행동을 시간대별로 관찰",
        "survey": "실천 경험, 불편함, 참여 의지, 효과가 크다고 보는 행동",
        "target": "학생, 환경 동아리 학생, 담당 교사, 급식실·시설 관리 담당자",
        "interview": "실천이 이어지지 않는 이유와 학교에서 바꾸기 쉬운 조건",
        "analysis": "실천 의지와 실제 행동의 차이를 비교하고, 장소별 문제 원인을 정리",
        "product": "학교 안에서 바로 실행할 수 있는 환경 실천 캠페인",
    },
    {
        "keywords": ["건강", "수면", "스트레스", "식습관", "급식", "보건", "다이어트", "생활습관"],
        "source": "청소년 건강 권장 기준, 보건 자료, 생활 습관 설문, 학교생활 사례",
        "field": "수면 시간, 식사 패턴, 운동 빈도, 스트레스 상황을 익명 기록표로 모으기",
        "survey": "습관 실천 정도, 어려운 이유, 몸과 마음의 변화, 도움받고 싶은 방식",
        "target": "생활 패턴이 다른 학생, 보건 교사, 담임 교사",
        "interview": "습관을 바꾸기 어려운 순간과 실제로 도움이 된 방법",
        "analysis": "습관 유형별로 만족도나 집중도 차이를 비교하고, 무리한 일반화는 피하기",
        "product": "학생이 부담 없이 실천할 수 있는 건강 루틴 제안",
    },
    {
        "keywords": ["친구", "관계", "소통", "학교생활", "수업", "학습", "공부", "진로", "직업", "동아리"],
        "source": "학생 경험 설문, 학교 규칙·활동 자료, 진로 정보, 학급 사례",
        "field": "상황별 어려움, 도움받은 방법, 참여 기회를 익명 사례 카드로 모으기",
        "survey": "만족도, 어려움의 빈도, 필요한 지원, 참여하고 싶은 방식",
        "target": "다양한 학년·역할의 학생, 담임 교사, 상담 또는 진로 담당 교사",
        "interview": "겉으로 드러난 문제 뒤에 있는 실제 이유와 필요한 지원",
        "analysis": "학생 집단별 요구 차이를 비교하고, 공통 요구와 특수한 요구를 분리",
        "product": "학급 규칙, 수업 참여 방식, 진로 활동 개선 제안",
    },
    {
        "keywords": ["패션", "소비", "브랜드", "유행", "가격", "가치소비", "여행", "맛집", "음식"],
        "source": "가격·브랜드 비교 자료, 후기와 광고 사례, 소비자 보호 자료, 문화 자료",
        "field": "선택 기준, 광고 문구, 가격 차이, 후기 신뢰도를 실제 사례로 비교",
        "survey": "구매·선택 기준, 유행 영향, 만족도, 후회 경험, 지속 가능성 고려 정도",
        "target": "선택 경험이 있는 학생, 소비를 줄이려는 학생, 관련 가게나 활동 경험자",
        "interview": "마지막 선택에서 가장 크게 작용한 정보와 감정",
        "analysis": "가격·유행·품질·가치 기준의 우선순위를 비교하고 선택 이유를 해석",
        "product": "합리적인 선택 기준표 또는 책임 있는 소비 안내문",
    },
    {
        "keywords": ["데이터", "통계", "그래프", "자료", "분석", "기록", "확률", "수학", "함수", "원주율", "방정식"],
        "source": "직접 수집한 표본 자료, 공개 통계, 그래프 사례, 측정 기준 설명",
        "field": "같은 기준으로 20개 이상 표본을 모으고 이상값과 누락값을 따로 표시",
        "survey": "응답 선택 이유, 예상과 실제의 차이, 자료 해석에서 헷갈린 점",
        "target": "자료를 만든 학생, 자료를 해석하는 학생, 수학 또는 정보 교사",
        "interview": "숫자만 봤을 때 놓칠 수 있는 맥락과 해석 기준",
        "analysis": "평균·비율·순위뿐 아니라 예외 사례와 표본의 한계를 함께 설명",
        "product": "해석 기준이 분명한 그래프와 자료 읽기 주의점",
    },
]


DEFAULT_GUIDE_PROFILE = {
    "source": "관련 설명 자료, 실제 사례, 학생 경험 자료, 학교에서 관찰할 수 있는 장면",
    "field": "주제와 관련된 행동·장소·상황을 정해 짧게 관찰 기록",
    "survey": "경험 여부, 중요하게 보는 기준, 어려운 점, 학교 적용 가능성",
    "target": "직접 경험한 학생, 경험이 적은 학생, 관련 교사 또는 담당자",
    "interview": "설문 선택지만으로 설명하기 어려운 이유와 실제 상황",
    "analysis": "응답을 기준별로 묶고 자료조사 내용과 학생 경험이 맞는지 비교",
    "product": "학교생활에서 적용할 수 있는 현실적인 제안",
}


def _guide_profile(topic: str) -> dict:
    lowered = topic.lower()
    scored = []
    for profile in GUIDE_PROFILES:
        score = sum(1 for keyword in profile["keywords"] if keyword.lower() in lowered)
        if score:
            scored.append((score, profile))
    scored.sort(key=lambda item: item[0], reverse=True)
    if len(scored) >= 2:
        primary = scored[0][1]
        secondary = scored[1][1]
        merged = dict(primary)
        merged["source"] = f"{primary['source']} / {secondary['source']}"
        merged["survey"] = f"{primary['survey']} + {secondary['survey']}"
        merged["target"] = f"{primary['target']} 또는 {secondary['target']}"
        merged["analysis"] = f"{primary['analysis']} 또한 {secondary['analysis']}"
        return merged
    if scored:
        return scored[0][1]
    return DEFAULT_GUIDE_PROFILE


def _topic_guidance(topic: str) -> dict:
    kind = _topic_kind(topic)
    terms = _topic_terms(topic)
    main = terms[0] if terms else topic
    second = terms[1] if len(terms) > 1 else "학교생활"
    inquiry_type, _, method_hint = TOPIC_METHOD_HINTS.get(kind, TOPIC_METHOD_HINTS["영향"])
    profile = _guide_profile(topic)
    return {
        "kind": kind,
        "main": main,
        "second": second,
        "method_hint": method_hint,
        "inquiry_type": inquiry_type,
        "profile": profile,
    }


def make_research_guide(topic: str) -> list[str]:
    g = _topic_guidance(topic)
    p = g["profile"]
    return [
        f"먼저 '{g['main']}'와 '{g['second']}'가 이 주제에서 어떤 뜻으로 쓰이는지 한 문장으로 정의하고, '{g['kind']}' 관점에서 볼 기준을 2~3개 정합니다.",
        f"자료조사는 '{p['source']}'에서 시작하세요. 자료마다 출처, 날짜, 핵심 근거, 내 주제와 연결되는 부분을 표로 적습니다.",
        f"현장 자료는 '{p['field']}' 방식으로 모아 보세요. 사진이 필요하면 개인정보가 나오지 않게 하고, 관찰 시간과 장소를 함께 기록합니다.",
        f"분석 방향은 '{g['method_hint']}'입니다. 특히 {p['analysis']}하도록 정리하면 주제에 맞는 근거가 더 분명해집니다.",
        f"자료조사 뒤에는 빈칸을 하나 찾습니다. 예: '{topic}'에서 자료만으로 알 수 없는 학생의 경험, 선택 이유, 실천 가능성은 무엇인가?",
    ]


def make_survey(topic: str) -> list[str]:
    g = _topic_guidance(topic)
    p = g["profile"]
    if g["kind"] == "비교":
        return [
            f"'{topic}'에서 비교할 두 대상이나 두 상황을 경험해 본 적이 있나요? 경험한 쪽과 경험하지 않은 쪽을 표시해 주세요.",
            f"두 대상을 비교할 때 가장 중요하다고 생각하는 기준은 무엇인가요? 예: {p['survey']}",
            f"본인의 경험을 기준으로 두 대상의 장점과 불편한 점을 각각 하나씩 적어 주세요.",
            "두 대상 중 학교생활에서 더 적용하기 쉬운 쪽은 무엇이라고 생각하나요? 이유도 적어 주세요.",
            f"결과를 그래프로 만들 때 어떤 기준으로 나누면 차이가 잘 보일까요? 예: 경험 여부, 빈도, 만족도, 걱정 정도",
        ]
    if g["kind"] == "개선":
        return [
            f"'{topic}'과 관련해 현재 가장 불편하거나 아쉬운 점은 무엇인가요?",
            f"그 문제가 생기는 가장 큰 이유는 무엇이라고 생각하나요? 아래 기준 중 가까운 것을 고르세요: {p['survey']}",
            "제안된 해결 방법이 실제 학교에서 가능하려면 어떤 조건이 필요할까요?",
            "해결 방법을 실행한다면 누가 가장 먼저 움직여야 한다고 보나요? 학생, 학급, 교사, 학교 중 골라 이유를 적어 주세요.",
            f"개선 결과를 확인하려면 어떤 자료를 다시 모아야 할까요? 예: 참여율, 만족도, 관찰 기록, 불편 감소 정도",
        ]
    if g["kind"] in {"안전", "윤리"}:
        return [
            f"'{topic}'과 관련해 가장 걱정되는 점은 무엇인가요?",
            f"안전하거나 공정하게 이용하기 위해 가장 중요한 기준은 무엇이라고 생각하나요? 예: {p['survey']}",
            "친구들이 이 기준을 잘 지키지 못하는 이유가 있다면 무엇일까요?",
            "규칙이 너무 엄격하면 생길 수 있는 문제와 너무 느슨하면 생길 수 있는 문제를 각각 하나씩 적어 주세요.",
            "학교나 학급에서 만들 수 있는 약속 또는 안내 문구를 하나 제안해 주세요.",
        ]
    if g["kind"] == "자료":
        return [
            f"'{topic}'에서 공통 특징으로 확인하고 싶은 항목은 무엇인가요? 예: {p['survey']}",
            "본인은 이 주제와 관련해 어떤 경험이나 관심을 가지고 있나요?",
            "비슷한 관심을 가진 친구들에게서 공통적으로 나타날 것 같은 특징은 무엇이라고 예상하나요?",
            "예상과 다른 응답이 나온다면 어떤 이유 때문일 수 있을까요?",
            "조사 결과를 표나 그래프로 정리한다면 어떤 기준으로 나누는 것이 좋을까요?",
        ]
    return [
        f"'{topic}'과 관련한 경험이 있나요? 있다면 어떤 경험인가요?",
        f"이 주제가 본인의 생활이나 학교생활에 어느 정도 영향을 준다고 생각하나요? 특히 {p['survey']} 중 어떤 부분과 관련이 큰가요?",
        "영향을 주는 가장 중요한 요인을 하나 고르고, 그렇게 생각한 실제 장면이나 이유를 적어 주세요.",
        "친구들의 응답이 나와 다를 수 있다고 생각하나요? 다르다면 어떤 점에서 다를까요?",
        f"조사 결과를 바탕으로 학교에서 실천할 수 있는 방법을 하나 제안해 주세요. 목표는 '{p['product']}'입니다.",
    ]


def make_interview(topic: str) -> list[str]:
    g = _topic_guidance(topic)
    p = g["profile"]
    return [
        f"인터뷰 대상은 {p['target']} 중에서 2명 이상으로 정해 보세요. 먼저 '{topic}'과 관련해 직접 겪었거나 본 장면을 자세히 말해 달라고 합니다.",
        f"그 장면에서 가장 크게 작용한 요인은 무엇이었나요? 답변을 들을 때는 '{p['interview']}'를 깊게 물어봅니다.",
        f"설문 응답만 보면 오해할 수 있는 부분은 무엇인가요? 선택한 답의 배경, 망설인 이유, 예외 상황을 추가로 질문합니다.",
        f"자료조사에서 찾은 내용과 실제 경험이 같았나요, 달랐나요? 달랐다면 왜 그런 차이가 생겼는지 물어봅니다.",
        f"마지막으로 학교에서 실천 가능한 제안을 하나 부탁하세요. 제안은 '{p['product']}' 형태로 정리하면 좋습니다.",
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
        "proposal": "중·고등학생이 무리 없이 실천할 수 있는 건강 습관 체크리스트",
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
# === 주제 일관성 강화 엔진 (QR 전용) ===
def _is_conceptual_topic(topic: str) -> bool:
    concepts = ["원리", "구조", "성립", "증명", "정의", "공식", "개념", "어떻게 작동", "메커니즘"]
    opinions = ["학생", "우리 반", "학교", "인식", "선호", "경험", "만족", "실태", "설문"]
    return any(x in topic for x in concepts) and not any(x in topic for x in opinions)


def _alignment_blueprint(topic: str) -> dict:
    p = _guide_profile(topic)
    shape = _report_inquiry_shape(topic)
    terms = ", ".join(_topic_terms(topic)[:4]) or topic
    conceptual = _is_conceptual_topic(topic)
    if conceptual:
        method = "교과서·공공기관·대학 자료에서 원리와 성립 조건을 확인하고, 대표 사례·반례·모형 또는 안전한 간이 실험으로 설명을 검토한다."
        evidence = "개념 정의, 작동 단계, 성립 조건, 대표 사례와 반례"
        analysis = "자료마다 같은 개념을 어떻게 정의하는지 비교하고, 원리의 각 단계가 사례에서 실제로 성립하는지 확인한다."
        caution = "학생 설문은 개념의 참·거짓을 증명하지 못하므로 오개념이나 이해도 확인을 위한 보조 자료로만 사용한다."
    elif any(x in topic for x in ["영향", "미치는", "효과", "관계"]):
        method = "원인 후보와 결과 지표를 각각 정해 같은 기간에 기록하고, 조건별 설문·관찰 결과와 신뢰할 수 있는 자료를 함께 비교한다."
        evidence = "원인 후보, 결과 지표, 비교 조건, 다른 영향을 줄 수 있는 요인"
        analysis = "조건별 빈도·비율·평균을 비교하되, 함께 변했다고 해서 원인이라고 단정하지 않고 다른 설명도 확인한다."
        caution = "상관관계를 인과관계로 단정하지 말고 수면, 학년, 기존 경험 등 숨은 요인을 기록한다."
    elif any(x in topic for x in ["비교", "차이", "전후"]):
        method = "비교 대상 두 가지와 공통 평가 기준 3개를 먼저 정하고, 같은 출처·기간·질문으로 자료를 수집한다."
        evidence = "비교 대상, 공통 기준, 조건별 수치와 사례"
        analysis = "공통점과 차이점을 같은 표에 놓고, 차이가 큰 기준부터 그 이유와 예외 사례를 해석한다."
        caution = "한쪽에만 유리한 기준을 고르지 말고 두 대상을 동일한 조건에서 비교한다."
    elif any(x in topic for x in ["개선", "해결", "제안", "캠페인", "아이디어"]):
        method = "문제 장면을 관찰하고 원인과 요구를 조사한 뒤, 효과·비용·안전·실행 가능성 기준으로 해결안을 평가한다."
        evidence = "문제 빈도, 불편을 겪는 대상, 기존 해결 사례, 실행 전후 확인 지표"
        analysis = "효과가 큰 안과 실행하기 쉬운 안을 구분해 점수표로 평가하고, 작은 범위에서 시험할 방법을 정한다."
        caution = "아이디어만 제시하지 말고 실행 주체, 기간, 비용, 확인 지표를 포함한다."
    elif any(x in topic for x in ["윤리", "공정", "안전", "신뢰", "개인정보"]):
        method = "이해관계자별 입장과 실제 사례를 조사하고, 권리·안전·공정성·실행 가능성이라는 동일 기준으로 판단한다."
        evidence = "찬반 근거, 영향을 받는 사람, 위험과 이익, 적용할 판단 기준"
        analysis = "입장별 근거를 기준표에 정리하고, 충돌하는 가치와 예외 상황을 함께 설명한다."
        caution = "찬반 인원수만으로 옳고 그름을 결정하지 말고 근거의 신뢰성과 영향을 함께 판단한다."
    else:
        method = f"{p['source']}에서 배경을 확인하고, {p['target']}을 대상으로 관찰·설문·인터뷰 중 주제에 맞는 방법을 선택한다."
        evidence = f"{terms}의 실제 사례, 빈도·조건·이유, 서로 다른 관점"
        analysis = p["analysis"]
        caution = "의견과 사실을 구분하고, 일부 응답을 전체 학생의 특징처럼 일반화하지 않는다."
    return {"terms": terms, "question": shape["question"], "method": method, "evidence": evidence,
            "analysis": analysis, "caution": caution, "sources": p["source"],
            "target": p["target"], "product": p["product"], "conceptual": conceptual}


def make_plan(topic: str) -> str:
    b = _alignment_blueprint(topic)
    return f"""# 탐구계획서

## 1. 주제와 범위
- 최종 주제: {topic}
- 끝까지 유지할 핵심어: {b['terms']}
- 먼저 핵심어의 뜻, 포함 범위, 제외 범위를 정한다.

## 2. 탐구 동기
이 주제와 연결되는 실제 생활·교과 장면 한 가지와 확인할 가치가 있는 이유를 3~4문장으로 쓴다.

## 3. 탐구 문제
- 핵심 질문: {b['question']}
- 세부 질문: 핵심어의 정의와 조건은 무엇인가? / 어떤 조건에서 차이가 큰가? / 근거로 어디까지 설명할 수 있는가?

## 4. 예상과 근거
- 예상: ___ / 예상 이유: ___
- 필요한 근거: {b['evidence']}
예상은 실제 결과가 아니며, 반대 결과와 예외도 그대로 기록한다.

## 5. 대상과 방법
- 권장 방법: {b['method']}
- 출처: {b['sources']}
- 대상: {b['target']}
설문은 가능하면 20명 이상, 인터뷰는 다른 관점의 2~3명, 관찰은 같은 기준으로 3회 이상 진행한다. 개념 탐구는 출처 3개 이상과 사례·반례를 비교한다.
기록표: 날짜/출처·대상/조건/확인한 사실/수치/해석/추가 확인점

## 6. 분석
{b['analysis']}
가장 큰 경향뿐 아니라 예상 밖의 값과 예외 사례도 표시한다.

## 7. 3주 일정
- 1주차: 핵심어 정의, 검색어 4개, 출처 3개, 조사 도구 초안
- 2주차: 조사 실행과 빠진 조건 보완
- 3주차: 표·그래프, 결론, 한계, 적용안, 보고서 완성

## 8. 윤리와 한계
{b['caution']}
개인정보를 받지 않고 익명·자발 참여를 안내한다. 예상 한계 2가지와 줄이는 방법을 적는다.

## 9. 산출물
{b['product']}와 보고서에 개념 정의, 근거 표, 그래프·사례 비교표, 결론의 근거, 한계를 넣는다.
"""


def make_research_guide(topic: str) -> list[str]:
    b = _alignment_blueprint(topic)
    return [
        f"1단계 주제 고정 — '{topic}'과 핵심어({b['terms']})의 뜻·포함 범위·제외 범위를 적으세요. — 산출물: 주제 범위표",
        f"2단계 질문·근거 연결 — '{b['question']}'에 답할 근거를 {b['evidence']}로 나누세요. — 산출물: 세부 질문/근거/수집법 연결표",
        f"3단계 검색 설계 — 핵심어에 원리·통계·사례·문제점·개선을 조합한 검색어 4개를 만들고 {b['sources']}를 우선하세요. — 산출물: 검색 기록",
        "4단계 출처 검증 — 기관·작성자, 제목, 발행일, URL, 확인일, 조사 대상과 정의를 적고 출처 3개 이상을 비교하세요. — 산출물: 신뢰도 점검표",
        f"5단계 맞춤 수집 — {b['method']} — 산출물: 사실/수치/사례/출처/연결 질문이 적힌 근거 카드",
        f"6단계 분석 — {b['analysis']} — 산출물: 제목·단위가 있는 표·그래프 또는 사례·반례 비교표",
        f"7단계 결론 점검 — 결론 문장마다 근거 번호를 붙이고 '{b['caution']}'을 확인하세요. — 산출물: 답할 수 있는 범위/한계/후속 질문/적용안",
    ]


def make_survey(topic: str) -> list[str]:
    b = _alignment_blueprint(topic)
    if b["conceptual"]:
        return [
            f"[안내] 이 설문은 '{topic}'의 진위를 결정하지 않고 이해와 오개념을 확인하는 보조 자료입니다. 익명이며 중단할 수 있습니다.",
            f"[사전 이해] '{b['terms']}'을 얼마나 설명할 수 있나요? (1 전혀 모름~5 설명 가능)",
            f"[개념 선택] '{topic}'을 가장 잘 설명하는 문장을 고르세요. (수업 자료로 정답 1개와 대표 오개념 2~3개 작성)",
            "[근거] 앞 문항을 선택한 이유는? (수업/직접 관찰/영상·인터넷/추측/기타)",
            f"[적용] '{topic}'의 원리를 새 사례에 적용하기 쉬웠나요? (1 매우 어려움~5 매우 쉬움)",
            "[변화] 자료를 본 뒤 생각이 바뀌었나요? (아니오/조금/많이) 무엇 때문인가요?",
            "[서술] 아직 이해되지 않는 단계나 반례를 적어 주세요.",
        ]
    return [
        f"[안내] '{topic}' 탐구를 위한 익명 설문입니다. 이름은 쓰지 않으며 원하지 않으면 중단할 수 있습니다.",
        f"[대상 조건] 주제와 직접 관련된 경험이 있나요? (없음/1~2회/월 1~3회/주 1회 이상/응답하지 않음)",
        f"[빈도] 최근 7일 동안 '{b['terms']}' 관련 행동·상황은 며칠 있었나요? (0~7일)",
        f"[정도] 그 경험이 주제의 핵심 결과에 미친 정도는? (1 전혀 그렇지 않다~5 매우 그렇다)",
        f"[조건] 결과가 가장 크게 달라지는 조건은? ({b['terms']}에 맞는 선택지 3~5개/기타)",
        "[이유] 앞 응답의 가장 큰 이유는? (개인/친구·가족/학교/정보·기술/비용·시간/기타)",
        f"[서술] '{topic}'에서 바뀌어야 할 점이나 예외 상황 한 가지를 적어 주세요. [분석: {b['analysis']}]",
    ]


def make_interview(topic: str) -> list[str]:
    b = _alignment_blueprint(topic)
    target = "관련 교과 교사·전문가와 서로 다른 이해 수준의 학생" if b["conceptual"] else b["target"]
    return [
        f"[대상·동의] {target} 중 다른 관점의 2~3명을 정하고 10~15분, 익명, 녹음 여부와 중단 가능성을 안내하세요.",
        f"[경험] '{topic}'과 관련한 구체적 장면을 말해 주세요. (언제, 어디서, 어떤 조건이었나요?)",
        f"[핵심 개념] '{b['terms']}'을 본인의 말로 설명해 주세요. (근거나 사례는 무엇인가요?)",
        "[원인·과정] 결과에 가장 중요했던 요인은 무엇인가요? (다른 조건이면 어떻게 달라질까요?)",
        "[근거 비교] 조사 자료와 경험이 같거나 다른 부분은? (차이가 생긴 이유는 무엇인가요?)",
        f"[예외·한계] 설명에 맞지 않는 사례나 주의점은? ({b['caution']})",
        f"[제안·분석] 더 확인할 자료나 실천안을 묻고, 답을 '{b['terms']}'별 공통점/차이점/예외/익명 인용으로 정리하세요.",
    ]


def make_report(topic: str, plan_text: str, log: str) -> str:
    b = _alignment_blueprint(topic)
    return f"""# {topic} 탐구 보고서 초안

## 1. 주제 적합성 핵심
- 최종 주제: {topic}
- 핵심어: {b['terms']}
- 핵심 질문: {b['question']}
- 필요한 근거: {b['evidence']}

## 2. 동기와 목적
실제 생활·교과 장면 ___에서 출발해, 주제를 소개하는 데 그치지 않고 핵심 질문에 근거로 답한다.

## 3. 이론적 배경
핵심어 정의: ___ [실제 출처 필요]
원리·배경·쟁점: ___
출처 기록: 기관/작성자, 제목, 발행일, URL, 확인일

## 4. 대상과 방법
권장 설계: {b['method']}
대상·표본/기간·장소/절차/윤리·안전: ___

## 5. 계획과 실행 비교
{_plan_excerpt(plan_text)}
실제로 달라진 점과 이유: ___

## 6. 실제 탐구 결과
{_student_notes(log)}
결과표 열: 자료·대상/조건/사실·수치/핵심 질문과의 관계/예외
[학생이 실제로 얻은 수치와 관찰만 입력]

## 7. 분석과 논의
{b['analysis']}
가장 분명한 근거/예상 밖 결과/자료 간 차이/다른 설명: ___
주의: {b['caution']}

## 8. 결론
핵심 질문의 답: ___
근거 1: ___ / 근거 2: ___
자료가 부족해 말할 수 없는 범위: ___

## 9. 한계와 후속 탐구
가장 큰 한계/줄이는 방법/다음 질문: ___

## 10. 학교 적용
실행 주체/행동/기간/효과 확인 지표/어려움과 대안: ___

## 11. 제출 전 확인
- [ ] 제목·질문·조사·분석·결론에 핵심어가 일관된다.
- [ ] 수치·인용·이미지에 실제 출처가 있다.
- [ ] 결과와 해석을 구분하고 근거보다 넓게 단정하지 않았다.
- [ ] 개인정보, 표·그래프 제목·단위, 맞춤법을 확인했다.
"""


# === 중·고등학생용 확장 관심사 30종 ===
# 각 관심사에 교과 연결, 핵심 쟁점, 대표 탐구 문제와 자료조사 전략을 함께 둔다.
EXTENDED_INTEREST_PROFILES = {
    "코딩": ("프로그램 설계와 문제 해결", "알고리즘, 오류 수정, 사용자 문제 해결"),
    "드론": ("드론 기술과 생활 활용", "비행 원리, 센서, 안전과 개인정보"),
    "우주": ("우주 과학과 미래 사회", "우주 환경, 탐사 기술, 사회적 가치"),
    "천문": ("천체 관측과 우주 이해", "관측 기록, 빛, 달과 별의 변화"),
    "의학": ("의학 정보와 청소년 건강", "예방, 치료, 근거 중심 건강 정보"),
    "뇌과학": ("뇌의 작동과 학습·행동", "기억, 주의, 보상과 습관"),
    "심리": ("청소년 심리와 의사 결정", "감정, 편향, 또래 관계와 대처"),
    "반려동물": ("반려동물 복지와 책임", "행동, 돌봄, 유기 예방"),
    "요리": ("조리 과학과 지속 가능한 식생활", "맛과 영양, 가열 변화, 음식물 쓰레기"),
    "제과제빵": ("발효와 식품 과학", "재료 비율, 발효 조건, 보관"),
    "사진": ("사진 표현과 기록 윤리", "빛과 구도, 보정, 초상권"),
    "디자인": ("사용자 중심 디자인", "정보 전달, 접근성, 학교 문제 개선"),
    "애니메이션": ("움직임 표현과 문화 콘텐츠", "프레임, 캐릭터, 사회문화 재현"),
    "드라마": ("영상 서사와 사회문화", "인물과 갈등, 청소년 재현, 사실과 각색"),
    "댄스": ("신체 표현과 공연 협업", "연습 효과, 부상 예방, 동작 동기화"),
    "악기": ("소리 과학과 음악 연습", "음색, 연습 방법, 합주 소통"),
    "e스포츠": ("경기 전략과 디지털 스포츠 문화", "팀 소통, 훈련, 공정한 경기 문화"),
    "자동차": ("미래 이동 기술과 안전", "에너지 효율, 안전 장치, 자율주행 윤리"),
    "건축": ("사람과 환경을 위한 공간", "채광과 환기, 구조 안전, 접근성"),
    "경제": ("생활 속 경제 현상", "물가, 수요와 공급, 체감 경제"),
    "창업": ("문제 해결형 창업", "수요 검증, 비용과 가격, 사회적 가치"),
    "금융": ("청소년 금융 생활", "복리, 소비 습관, 투자 위험과 정보 신뢰"),
    "역사": ("사료로 해석하는 역사", "관점, 생활사, 역사 기억"),
    "문화유산": ("문화유산 보존과 활용", "디지털 복원, 관광과 보존, 지역 유산"),
    "언어": ("언어 변화와 소통", "신조어, 높임말, 다언어 정보"),
    "영어": ("영어 학습과 실제 의사소통", "자막, 번역, 반복 말하기"),
    "글쓰기": ("생각을 구조화하는 글쓰기", "개요, 근거, 피드백과 수정"),
    "토론": ("근거 중심 토론과 숙의", "출처, 반론, 공정한 발언 규칙"),
    "봉사활동": ("지역 문제와 참여", "수요자 중심, 지속성, 학교 연계"),
    "안전": ("학교와 생활 속 위험 예방", "통학, 재난, 실험·체육 안전"),
}
INTEREST_PROFILES.update(EXTENDED_INTEREST_PROFILES)

CUSTOM_INTEREST_KEYWORDS.extend([
    ("코딩", "코딩"), ("프로그래밍", "코딩"), ("드론", "드론"), ("우주", "우주"),
    ("천문", "천문"), ("별", "천문"), ("의학", "의학"), ("뇌", "뇌과학"),
    ("심리", "심리"), ("반려동물", "반려동물"), ("요리", "요리"), ("제과", "제과제빵"),
    ("제빵", "제과제빵"), ("사진", "사진"), ("디자인", "디자인"), ("애니메이션", "애니메이션"),
    ("드라마", "드라마"), ("댄스", "댄스"), ("악기", "악기"), ("e스포츠", "e스포츠"),
    ("자동차", "자동차"), ("건축", "건축"), ("경제", "경제"), ("창업", "창업"),
    ("금융", "금융"), ("역사", "역사"), ("문화유산", "문화유산"), ("언어", "언어"),
    ("영어", "영어"), ("글쓰기", "글쓰기"), ("토론", "토론"), ("봉사", "봉사활동"),
    ("안전", "안전"),
])

_EXTENDED_CURATED_TOPICS = {
    "코딩": [
        ("학교생활의 불편을 해결하는 코딩 프로그램은 어떤 절차로 설계해야 할까?", "정보", "개선", 4),
        ("같은 문제에서 블록 코딩과 텍스트 코딩의 이해도와 오류율은 어떻게 다를까?", "정보", "비교", 3),
        ("코딩 오류 기록을 분석하면 디버깅 시간을 줄일 수 있을까?", "정보", "자료", 3),
    ],
    "드론": [
        ("드론의 무게 중심과 바람 세기는 비행 안정성에 어떤 영향을 줄까?", "기술", "영향", 4),
        ("학교에서 드론 촬영을 할 때 필요한 안전·개인정보 기준은 무엇일까?", "도덕", "안전", 3),
        ("드론 센서 자료를 학교 시설 점검에 활용하는 방법은 무엇일까?", "기술", "개선", 4),
    ],
    "우주": [
        ("우주 쓰레기는 인공위성과 미래 우주 탐사에 어떤 위험을 만들까?", "과학", "영향", 3),
        ("장기 우주생활에서 청소년이 주목할 건강 문제와 해결 기술은 무엇일까?", "과학", "개선", 4),
        ("우주개발 비용과 과학·사회적 가치를 어떤 기준으로 비교해야 할까?", "사회", "비교", 4),
    ],
    "천문": [
        ("한 달간 달의 모양과 뜨는 시간을 관찰하면 어떤 규칙을 찾을 수 있을까?", "과학", "자료", 4),
        ("우리 지역의 광공해는 별 관측에 얼마나 영향을 줄까?", "과학", "영향", 3),
        ("별의 색과 표면 온도 자료 사이에는 어떤 관계가 있을까?", "과학", "자료", 3),
    ],
    "의학": [
        ("청소년 건강 정보를 믿을 수 있는지 판단하는 기준은 무엇일까?", "보건", "자료", 3),
        ("항생제 오남용은 개인과 사회에 어떤 문제를 만들까?", "보건", "영향", 3),
        ("청소년 질병에서 예방과 치료의 효과·비용을 어떻게 비교할 수 있을까?", "보건", "비교", 4),
    ],
    "뇌과학": [
        ("수면 시간과 학습 내용 기억 정도에는 어떤 관계가 있을까?", "과학", "영향", 3),
        ("스마트폰 멀티태스킹은 주의 집중과 과제 수행에 어떤 영향을 줄까?", "과학", "영향", 3),
        ("보상 방식은 공부 습관을 형성하고 유지하는 데 어떤 차이를 만들까?", "과학", "비교", 4),
    ],
    "심리": [
        ("시험 불안을 낮추는 방법 중 학생이 실천하기 쉬운 것은 무엇일까?", "보건", "개선", 3),
        ("확증편향은 뉴스와 정보를 선택하고 판단하는 데 어떤 영향을 줄까?", "도덕", "영향", 3),
        ("또래 압력을 받을 때 건강하게 의사결정하는 방법은 무엇일까?", "도덕", "개선", 3),
    ],
    "반려동물": [
        ("행동 풍부화 활동은 반려동물의 스트레스 행동에 어떤 변화를 줄까?", "과학", "영향", 4),
        ("청소년이 반려동물을 기르기 전에 확인해야 할 책임과 비용은 무엇일까?", "도덕", "자료", 3),
        ("지역 유기동물을 줄이기 위해 학교가 실천할 수 있는 방법은 무엇일까?", "사회", "개선", 4),
    ],
    "요리": [
        ("조리 방법에 따라 같은 식재료의 맛과 영양은 어떻게 달라질까?", "기술가정", "비교", 3),
        ("가열 온도와 시간은 식품의 색·식감 변화에 어떤 영향을 줄까?", "과학", "영향", 3),
        ("급식 잔반을 줄이면서 영양을 지키는 요리 아이디어는 무엇일까?", "기술가정", "개선", 4),
    ],
    "제과제빵": [
        ("발효 온도와 시간은 빵의 부피와 식감에 어떤 영향을 줄까?", "과학", "영향", 4),
        ("설탕과 지방 비율을 바꾸면 쿠키의 맛과 질감은 어떻게 달라질까?", "과학", "비교", 3),
        ("빵의 신선도를 오래 유지하는 포장과 보관 방법은 무엇일까?", "기술가정", "개선", 3),
    ],
    "사진": [
        ("사진의 구도와 빛은 보는 사람의 감정 해석에 어떤 차이를 만들까?", "미술", "영향", 3),
        ("사진 보정은 어디까지 허용해야 기록의 신뢰성을 지킬 수 있을까?", "도덕", "윤리", 3),
        ("학교 기록 사진을 안전하게 공유하기 위한 초상권 기준은 무엇일까?", "도덕", "안전", 3),
    ],
    "디자인": [
        ("색과 글꼴 선택은 학교 안내문의 정보 이해도에 어떤 영향을 줄까?", "미술", "영향", 3),
        ("색각·시각 차이를 고려한 유니버설 디자인 기준은 무엇일까?", "미술", "개선", 4),
        ("학생 동선을 개선하는 학교 공간 안내 디자인은 어떻게 만들 수 있을까?", "미술", "개선", 4),
    ],
    "애니메이션": [
        ("프레임 속도에 따라 움직임의 자연스러움은 어떻게 달라질까?", "미술", "비교", 3),
        ("캐릭터의 표정과 색은 시청자의 공감에 어떤 영향을 줄까?", "미술", "영향", 3),
        ("애니메이션의 직업·문화 재현에서 고정관념을 줄이는 방법은 무엇일까?", "사회", "개선", 4),
    ],
    "드라마": [
        ("청소년 드라마는 학교 문제를 얼마나 현실적으로 재현하고 있을까?", "국어", "자료", 3),
        ("회차 끝의 긴장 장치는 다음 회 시청 의도에 어떤 영향을 줄까?", "국어", "영향", 3),
        ("역사 드라마에서 사실과 각색의 경계는 어떤 기준으로 판단해야 할까?", "역사", "윤리", 4),
    ],
    "댄스": [
        ("영상 피드백을 활용한 반복 연습은 동작 정확도에 어떤 영향을 줄까?", "체육", "영향", 4),
        ("댄스 전 준비운동은 부상 위험을 줄이는 데 어떤 도움이 될까?", "체육", "안전", 3),
        ("단체 댄스의 동작 동기화를 높이는 의사소통 방법은 무엇일까?", "체육", "개선", 3),
    ],
    "악기": [
        ("짧게 나누어 연습하기와 몰아서 연습하기의 연주 정확도는 어떻게 다를까?", "음악", "비교", 3),
        ("악기의 재질과 길이는 음높이와 음색에 어떤 영향을 줄까?", "음악", "영향", 3),
        ("학교 합주의 완성도를 높이는 연습·의사소통 방법은 무엇일까?", "음악", "개선", 4),
    ],
    "e스포츠": [
        ("팀 의사소통 방식은 e스포츠 경기력에 어떤 영향을 줄까?", "체육", "영향", 3),
        ("훈련 시간과 수면 습관은 반응 속도와 집중력에 어떤 관계가 있을까?", "보건", "자료", 4),
        ("공정하고 존중받는 e스포츠 문화를 위한 경기 규칙은 무엇일까?", "도덕", "개선", 3),
    ],
    "자동차": [
        ("전기자동차와 내연기관 자동차의 에너지 효율과 환경 영향은 어떻게 다를까?", "기술", "비교", 4),
        ("안전벨트와 충돌 방지 장치는 탑승자를 어떤 원리로 보호할까?", "과학", "안전", 3),
        ("자율주행 자동차의 사고 판단에는 어떤 윤리 기준이 필요할까?", "도덕", "윤리", 4),
    ],
    "건축": [
        ("교실의 채광과 환기 조건은 학습 환경에 어떤 영향을 줄까?", "기술", "영향", 4),
        ("건물 모형의 구조에 따라 지진 흔들림을 견디는 정도는 어떻게 다를까?", "과학", "비교", 4),
        ("모든 학생이 편리하게 이용하는 학교 공간의 설계 기준은 무엇일까?", "기술", "개선", 4),
    ],
    "경제": [
        ("물가 변화는 청소년의 용돈 사용과 구매 선택에 어떤 영향을 줄까?", "사회", "영향", 3),
        ("학교 매점 상품의 가격과 수요 사이에는 어떤 관계가 있을까?", "사회", "자료", 3),
        ("경제지표와 학생이 느끼는 체감 경제는 왜 다를 수 있을까?", "사회", "비교", 4),
    ],
    "창업": [
        ("학생 생활의 불편을 해결하는 창업 아이디어의 수요는 어떻게 검증할까?", "진로", "자료", 4),
        ("제품의 비용과 학생이 지불할 가격을 함께 고려하는 방법은 무엇일까?", "사회", "개선", 4),
        ("수익과 환경·사회적 가치를 함께 만드는 학생 창업 모델은 무엇일까?", "진로", "개선", 4),
    ],
    "금융": [
        ("저축 기간과 이자율에 따라 복리 효과는 얼마나 달라질까?", "수학", "자료", 3),
        ("간편결제 사용은 청소년의 충동구매와 소비 기록에 어떤 영향을 줄까?", "사회", "영향", 3),
        ("온라인 투자 정보의 신뢰도와 위험을 판단하는 기준은 무엇일까?", "사회", "안전", 4),
    ],
    "역사": [
        ("같은 사건을 다룬 1차 사료와 교과서의 관점은 어떻게 다를까?", "역사", "비교", 4),
        ("과거 청소년의 학교·일상생활은 오늘날과 어떻게 달랐을까?", "역사", "비교", 3),
        ("지역의 역사적 사건을 기억하고 전달하는 방법은 왜 달라질까?", "역사", "자료", 3),
    ],
    "문화유산": [
        ("디지털 기록과 3D 복원은 문화유산 보존에 어떤 도움과 한계를 가질까?", "역사", "비교", 4),
        ("문화유산 관광과 보존의 균형을 위한 기준은 무엇일까?", "사회", "개선", 4),
        ("학교 주변 문화유산을 청소년에게 알리는 효과적인 방법은 무엇일까?", "역사", "개선", 3),
    ],
    "언어": [
        ("청소년 신조어는 어떤 경로로 생겨나고 퍼질까?", "국어", "자료", 3),
        ("높임말 사용은 세대와 상황에 따라 어떻게 달라질까?", "국어", "비교", 3),
        ("학교의 다언어 안내는 외국인 학생의 정보 이해를 어떻게 도울 수 있을까?", "국어", "개선", 4),
    ],
    "영어": [
        ("영어 영상의 자막 유무는 듣기 이해와 어휘 기억에 어떤 차이를 만들까?", "영어", "비교", 3),
        ("AI 번역과 학생 번역의 정확성·자연스러움은 어떻게 다를까?", "영어", "비교", 4),
        ("짧은 영어 반복 말하기는 말하기 자신감에 어떤 영향을 줄까?", "영어", "영향", 3),
    ],
    "글쓰기": [
        ("개요 작성 여부는 글의 논리성과 완성도에 어떤 차이를 만들까?", "국어", "비교", 3),
        ("동료 피드백은 초고를 수정하고 근거를 보강하는 데 어떤 도움을 줄까?", "국어", "영향", 3),
        ("AI 도움 글과 직접 쓴 글을 책임 있게 구분·활용하는 기준은 무엇일까?", "국어", "윤리", 4),
    ],
    "토론": [
        ("토론 근거의 출처를 확인하는 기준은 결론의 신뢰도를 어떻게 높일까?", "국어", "자료", 3),
        ("상대의 반론을 요약한 뒤 답하는 방식은 토론의 질에 어떤 영향을 줄까?", "국어", "영향", 3),
        ("모든 참여자가 발언하는 공정한 교실 토론 규칙은 무엇일까?", "도덕", "개선", 3),
    ],
    "봉사활동": [
        ("일회성 봉사와 지속적 봉사는 지역 문제 해결 효과가 어떻게 다를까?", "사회", "비교", 4),
        ("봉사 수요자의 의견을 반영하는 활동 설계 방법은 무엇일까?", "사회", "개선", 3),
        ("학생의 강점과 지역의 필요를 연결한 학교 봉사활동은 무엇일까?", "진로", "개선", 4),
    ],
    "안전": [
        ("학교 주변 통학로의 위험 지점과 개선 우선순위는 어떻게 정할까?", "사회", "안전", 4),
        ("재난 대피훈련의 이해도와 실제 대응력을 높이는 방법은 무엇일까?", "안전", "개선", 3),
        ("과학실·체육 활동 사고를 줄이기 위한 행동 기준은 무엇일까?", "안전", "개선", 3),
    ],
}
CURATED_SINGLE_TOPICS.update(_EXTENDED_CURATED_TOPICS)

GUIDE_PROFILES.extend([
    {
        "keywords": ["코딩", "프로그램", "드론", "자동차", "건축", "센서", "자율주행"],
        "source": "과학기술 공공기관 자료, 제품 안전 기준, 설계 사례, 직접 측정·관찰 기록",
        "method": "작동 원리와 사용 상황을 나누고, 조건을 하나씩 바꿔 결과를 같은 기준으로 기록한다.",
        "evidence": "정확성, 안전성, 효율, 사용자 편의, 실제 구현 가능성을 비교한다.",
        "keywords_hint": "검색어 예: 작동 원리, 안전 기준, 설계 과정, 조건별 측정 결과",
    },
    {
        "keywords": ["우주", "천문", "별", "달", "광공해", "우주 쓰레기"],
        "source": "한국천문연구원·우주항공 기관 자료, 관측 자료, 과학 교과서와 연구기관 설명",
        "method": "관측 날짜·장소·조건을 기록하고, 공개 과학 자료와 직접 관찰 결과를 함께 비교한다.",
        "evidence": "관측 조건, 자료의 시기, 측정 단위, 과학적 설명의 일치 여부를 확인한다.",
        "keywords_hint": "검색어 예: 천체 관측 자료, 달 위상, 광공해 측정, 우주 환경",
    },
    {
        "keywords": ["의학", "뇌", "심리", "기억", "불안", "주의", "건강 정보"],
        "source": "질병관리청·보건기관 자료, 청소년 건강 통계, 대학·연구기관의 쉬운 과학 설명",
        "method": "상관관계와 인과관계를 구분하고, 개인 진단이 아닌 익명 설문·공개 자료 중심으로 조사한다.",
        "evidence": "연구 대상, 표본 수, 출처, 생활 적용 가능성, 개인정보 보호를 확인한다.",
        "keywords_hint": "검색어 예: 청소년 건강 통계, 기억과 수면 연구, 심리 대처 방법",
    },
    {
        "keywords": ["요리", "제과", "제빵", "발효", "조리", "식재료"],
        "source": "식품안전 기관 자료, 영양 정보, 조리 과학 자료, 조건별 조리 관찰 기록",
        "method": "재료의 양·온도·시간 중 한 조건만 바꾸고 맛·색·질감·부피를 같은 척도로 기록한다.",
        "evidence": "식품 안전, 영양, 측정 조건, 반복 결과, 실생활 적용성을 비교한다.",
        "keywords_hint": "검색어 예: 조리 온도 변화, 발효 조건, 식품 보관, 영양 성분",
    },
    {
        "keywords": ["사진", "디자인", "애니메이션", "드라마", "댄스", "악기", "구도", "음색"],
        "source": "문화예술 기관 자료, 작품·공연 사례, 제작 원리 자료, 관객 반응 설문",
        "method": "표현 요소를 하나씩 구분하고 두 사례를 같은 감상·기술 기준표로 비교한다.",
        "evidence": "표현 효과, 제작 의도, 관객 반응, 저작권·초상권, 문화적 맥락을 살핀다.",
        "keywords_hint": "검색어 예: 표현 기법 효과, 제작 과정, 관객 반응, 저작권 기준",
    },
    {
        "keywords": ["e스포츠", "경기력", "팀 의사소통", "반응 속도"],
        "source": "경기 기록, 스포츠 과학 자료, 선수 훈련 사례, 게임 운영 정책",
        "method": "승패만 보지 않고 의사소통·반응·수면·훈련량을 나누어 기록하고 비교한다.",
        "evidence": "경기 기록, 건강, 공정성, 팀워크, 재현 가능한 훈련 조건을 확인한다.",
        "keywords_hint": "검색어 예: e스포츠 훈련, 팀 의사소통, 반응 속도, 공정 경기",
    },
    {
        "keywords": ["경제", "창업", "금융", "물가", "가격", "복리", "투자"],
        "source": "한국은행·금융감독원·통계청 자료, 시장 가격 조사, 청소년 금융교육 자료",
        "method": "가격·비용·수요·위험을 숫자로 정리하고 실제 생활 사례와 공공 통계를 비교한다.",
        "evidence": "자료 시점, 표본, 비용과 편익, 위험, 이해관계자 영향을 확인한다.",
        "keywords_hint": "검색어 예: 청소년 소비 통계, 물가 지표, 복리 계산, 창업 수요 조사",
    },
    {
        "keywords": ["역사", "문화유산", "사료", "복원", "지역 유산"],
        "source": "국가기록원·문화유산 기관 자료, 박물관 자료, 1차 사료와 지역 구술 기록",
        "method": "누가 언제 왜 만든 자료인지 확인하고 서로 다른 관점의 사료를 교차 비교한다.",
        "evidence": "작성 시기, 작성자 관점, 사실 근거, 보존 가치, 현재적 의미를 살핀다.",
        "keywords_hint": "검색어 예: 1차 사료, 지역사 기록, 문화유산 보존, 디지털 복원",
    },
    {
        "keywords": ["언어", "영어", "글쓰기", "토론", "신조어", "자막", "번역", "피드백"],
        "source": "국립국어원·교육기관 자료, 실제 언어 사례, 학습 전후 기록, 토론 자료",
        "method": "사용 맥락과 대상을 정한 뒤 문장·발언·학습 결과를 같은 기준표로 비교한다.",
        "evidence": "표현의 정확성, 이해도, 논리성, 출처 신뢰도, 소통 효과를 확인한다.",
        "keywords_hint": "검색어 예: 청소년 언어 사용, 영어 학습 효과, 글쓰기 피드백, 토론 근거",
    },
    {
        "keywords": ["반려동물", "봉사", "안전", "통학로", "재난", "유기동물"],
        "source": "지자체·공공기관 자료, 학교 안전 기록, 지역 현장 관찰, 관계자 인터뷰",
        "method": "문제 당사자의 필요와 위험 지점을 먼저 확인하고 빈도·심각도·실천 가능성을 기록한다.",
        "evidence": "안전, 대상자 의견, 지속 가능성, 비용, 학교·지역에서의 실행 가능성을 비교한다.",
        "keywords_hint": "검색어 예: 학교 안전 통계, 지역 봉사 수요, 동물복지 기준, 통학로 개선",
    },
])


# 최종 탐구 생성기는 아래 필드를 공통으로 사용한다. 확장 프로필에도 단계별 산출물을 명시한다.
for _profile in GUIDE_PROFILES:
    _profile.setdefault("target", "중·고등학생, 교사 또는 학교·지역의 관련 사례")
    _profile.setdefault("field", _profile["method"])
    _profile.setdefault(
        "analysis",
        f"{_profile['evidence']}를 기준으로 표를 만들고, 공통점·차이·예외와 그 이유를 해석한다.",
    )
    _profile.setdefault(
        "survey",
        "경험 빈도와 현재 상태, 원인 인식, 영향, 개선안의 필요도·실천 의향을 한 문항에 한 가지씩 묻는다.",
    )
    _profile.setdefault(
        "interview",
        "실제 경험, 구체적 사례, 원인, 기존 대응, 가장 현실적인 개선안과 확인 지표를 차례로 질문한다.",
    )
    _profile.setdefault(
        "product",
        "핵심 근거 표·그래프, 사례 비교, 결론, 학생이 실천할 수 있는 제안을 담은 탐구 보고서",
    )

_EXTENDED_SUBJECTS = {
    "코딩": "정보", "드론": "기술", "우주": "과학", "천문": "과학",
    "의학": "보건", "뇌과학": "과학", "심리": "도덕", "반려동물": "과학",
    "요리": "기술가정", "제과제빵": "기술가정", "사진": "미술", "디자인": "미술",
    "애니메이션": "미술", "드라마": "국어", "댄스": "체육", "악기": "음악",
    "e스포츠": "체육", "자동차": "기술", "건축": "기술", "경제": "사회",
    "창업": "진로", "금융": "사회", "역사": "역사", "문화유산": "역사",
    "언어": "국어", "영어": "영어", "글쓰기": "국어", "토론": "국어",
    "봉사활동": "사회", "안전": "안전",
}
_BASE_SUBJECT_FOR = _subject_for

def _subject_for(info: dict) -> str:
    return _EXTENDED_SUBJECTS.get(info["category"], _BASE_SUBJECT_FOR(info))
