import tempfile
from pathlib import Path

import database
import settings_store
from fastapi.testclient import TestClient
from offline_engine import (
    make_interview,
    make_plan,
    make_report,
    make_research_guide,
    make_survey,
    recommend_topics,
)


def assert_offline_generators():
    base_interests = [
        ("AI", ""), ("환경", "플라스틱"), ("스포츠", "수면"),
        ("수학", "원주율"), ("학교생활", "친구관계"), ("진로", "로봇"),
    ]
    added_interests = [
        "코딩", "드론", "우주", "천문", "의학", "뇌과학", "심리", "반려동물",
        "요리", "제과제빵", "사진", "디자인", "애니메이션", "드라마", "댄스", "악기",
        "e스포츠", "자동차", "건축", "경제", "창업", "금융", "역사", "문화유산",
        "언어", "영어", "글쓰기", "토론", "봉사활동", "안전",
    ]
    assert len(added_interests) == 30 and len(set(added_interests)) == 30
    interests = base_interests + [(interest, "") for interest in added_interests]
    checked = 0
    for tag, detail in interests:
        items = recommend_topics(tag, detail)
        assert len(items) >= 10, (tag, detail, len(items))
        sample_size = 3 if tag in added_interests else 10
        if tag in added_interests:
            assert len({item["topic"] for item in items[:3]}) == 3, tag
            assert all(item["subject"] and item["reason"] and item["fit"]["total"] > 0 for item in items[:3]), tag
        for item in items[:sample_size]:
            topic = item["topic"]
            plan = make_plan(topic)
            guide = make_research_guide(topic)
            survey = make_survey(topic)
            interview = make_interview(topic)
            report = make_report(topic, plan, "실제 조사 메모")
            assert len(plan) > 500 and topic in plan
            assert len(guide) >= 7
            assert len(survey) >= 7
            assert len(interview) >= 7
            assert len(report) > 700 and topic in report
            checked += 1
    return checked



def assert_ai_recommend_contract():
    import ai_engine
    original_config = ai_engine.get_online_config
    original_call = ai_engine._compact_call
    fake_items = [
        {
            "topic": f"점검용 탐구 주제 {index}",
            "subject": "사회",
            "difficulty": "중",
            "inquiry_type": "자료조사",
            "duration": "3주",
            "reason": "자료와 비교 기준을 확인한다.",
            "fit": {"data_collection": 80, "survey": 60, "experiment": 20, "school_application": 70, "total": 70},
        }
        for index in range(15)
    ]
    ai_engine.get_online_config = lambda: {"enabled": True, "api_key": "sk-test-key-long-enough-value", "model": "test-model"}
    ai_engine._compact_call = lambda *args, **kwargs: __import__("json").dumps(fake_items, ensure_ascii=False)
    result = ai_engine.recommend("게임", "")
    assert result["mode"] == "online" and len(result["items"]) == 15

    ai_engine._compact_call = lambda *args, **kwargs: (_ for _ in ()).throw(ValueError("internal JSON { detail }"))
    fallback = ai_engine.recommend("게임", "")
    assert fallback["mode"] == "offline" and fallback.get("ai_error")
    assert "internal JSON" not in fallback["ai_error"]
    ai_engine.get_online_config = original_config
    ai_engine._compact_call = original_call

def assert_api_flow():
    with tempfile.TemporaryDirectory() as temp_dir:
        data_dir = Path(temp_dir)
        database.DATA_DIR = data_dir
        database.DB_PATH = data_dir / "inquiry_mate.db"
        settings_store.SETTINGS_PATH = data_dir / "settings.json"
        settings_store.USAGE_PATH = data_dir / "ai_usage.json"

        import main

        database.init_db()
        with TestClient(main.app) as client:
            assert client.get("/api/class-info").status_code == 200
            assert client.get("/student.html").status_code == 200
            assert client.get("/teacher.html").status_code == 200
            assert client.get("/wizard.html").status_code == 200

            status = client.get("/api/teacher/password-status").json()
            if not status["has_password"]:
                response = client.post(
                    "/api/teacher/password",
                    json={"password": "teacher1234", "hint": "smoke", "current_password": ""},
                )
                assert response.status_code == 200, response.text
            login = client.post("/api/teacher/login", json={"password": "teacher1234"})
            assert login.status_code == 200 and login.json()["ok"]

            ai_settings = client.post(
                "/api/teacher/ai-settings", json={"password": "teacher1234"}
            )
            assert ai_settings.status_code == 200, ai_settings.text

            student = client.post(
                "/api/student/login", json={"name": "점검학생", "student_no": "99999"}
            )
            assert student.status_code == 200, student.text
            student_id = student.json()["id"]

            recommended = client.post(
                "/api/recommend", json={"tag": "환경", "detail": "플라스틱"}
            )
            assert recommended.status_code == 200, recommended.text
            result = recommended.json()
            assert result["mode"] == "offline"
            assert len(result["items"]) >= 10
            item = result["items"][0]

            created = client.post(
                "/api/projects",
                json={
                    "student_id": student_id,
                    "tag": "환경",
                    "interest": "플라스틱",
                    "topic": item["topic"],
                    "subject": item.get("subject", ""),
                    "fit_score": item["fit"]["total"],
                    "custom_topic": False,
                },
            )
            assert created.status_code == 200, created.text
            project_id = created.json()["project_id"]

            original_settings_reader = main.get_ai_settings_public
            original_ai_plan = main.ai_engine.plan
            main.get_ai_settings_public = lambda: {"online_ai_enabled": True, "has_api_key": True}
            main.ai_engine.plan = lambda topic: (_ for _ in ()).throw(AssertionError("custom topic must not call OpenAI plan"))
            custom = client.post(
                "/api/projects",
                json={
                    "student_id": student_id,
                    "tag": "직접 주제",
                    "interest": "학교 숲",
                    "topic": "학교 숲의 온도 저감 효과와 학생 휴식 공간 개선",
                    "subject": "자율탐구",
                    "fit_score": 80,
                    "custom_topic": True,
                },
            )
            main.get_ai_settings_public = original_settings_reader
            main.ai_engine.plan = original_ai_plan
            assert custom.status_code == 200, custom.text
            custom_id = custom.json()["project_id"]
            assert client.get(f"/api/projects/{custom_id}").json()["plan"]
            assert client.delete(f"/api/projects/{custom_id}").status_code == 200

            usage = client.post("/api/teacher/ai-usage", json={"password": "teacher1234"})
            assert usage.status_code == 200
            assert usage.json()["totals"]["api_calls"] == 0

            project = client.get(f"/api/projects/{project_id}")
            assert project.status_code == 200 and project.json()["plan"]
            for suffix in ["guide", "survey", "interview"]:
                response = client.get(f"/api/projects/{project_id}/{suffix}")
                assert response.status_code == 200, response.text
                assert len(response.json()["items"]) >= 7

            payload = {
                "plan": project.json()["plan"],
                "plan_note": "계획 메모",
                "guide_note": "자료 메모",
                "survey_note": "설문 메모",
                "interview_note": "인터뷰 메모",
                "research_log": "탐구일지",
                "progress_note": "통합 점검 진행",
                "report": "",
                "report_note": "",
                "progress": 80,
            }
            updated = client.put(f"/api/projects/{project_id}", json=payload)
            assert updated.status_code == 200, updated.text

            report = client.post(f"/api/projects/{project_id}/report")
            assert report.status_code == 200, report.text
            assert len(report.json()["report"]) > 700

            progress = client.put(
                f"/api/projects/{project_id}/progress-note",
                json={"progress_note": "진행 상황 저장 점검"},
            )
            assert progress.status_code == 200

            feedback = client.post(
                f"/api/projects/{project_id}/feedback",
                json={
                    "teacher_comment": "점검 완료",
                    "problem_def": 5,
                    "data_collection": 4,
                    "analysis": 4,
                    "communication": 5,
                },
            )
            assert feedback.status_code == 200 and feedback.json()["total_score"] == 18

            dashboard = client.get("/api/teacher/dashboard")
            assert dashboard.status_code == 200
            assert any(row["id"] == project_id for row in dashboard.json()["items"])

            projects = client.get(f"/api/student/{student_id}/projects")
            assert projects.status_code == 200 and projects.json()["items"]

            deleted = client.delete(f"/api/projects/{project_id}")
            assert deleted.status_code == 200


if __name__ == "__main__":
    count = assert_offline_generators()
    assert_ai_recommend_contract()
    assert_api_flow()
    print(f"QR smoke test passed: {count} offline topics and full API flow")
