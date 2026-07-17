import io
import os
import secrets
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import qrcode
import qrcode.image.svg

import ai_engine
from database import get_conn, init_db
from offline_engine import make_plan as make_offline_plan
from settings_store import (
    get_ai_settings_public,
    get_ai_usage_stats,
    get_teacher_auth_public,
    recover_teacher_password,
    reset_ai_usage_stats,
    save_ai_settings,
    set_ai_mode_enabled,
    save_teacher_password,
    verify_teacher_password,
)

BASE_DIR = Path(__file__).resolve().parent.parent
RESOURCE_DIR = Path(getattr(sys, "_MEIPASS", BASE_DIR))
FRONTEND_DIR = RESOURCE_DIR / "frontend"
KST = timezone(timedelta(hours=9))
TEACHER_SESSION_HOURS = 4
teacher_sessions: dict[str, datetime] = {}

app = FastAPI(title="AI 탐구메이트")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


class LoginReq(BaseModel):
    name: str
    student_no: str


class ClassModeReq(BaseModel):
    enabled: bool = False


class RecommendReq(BaseModel):
    tag: str
    detail: str = ""


class ProjectReq(BaseModel):
    student_id: int
    tag: str
    interest: str
    topic: str
    subject: str = ""
    fit_score: int = 0
    custom_topic: bool = False


class UpdateProjectReq(BaseModel):
    plan: str = ""
    plan_note: str = ""
    guide_note: str = ""
    survey_note: str = ""
    interview_note: str = ""
    research_log: str = ""
    progress_note: str = ""
    report: str = ""
    report_note: str = ""
    progress: int = 10


class ProgressNoteReq(BaseModel):
    progress_note: str = ""


class AiSettingsReq(BaseModel):
    password: str = ""
    online_ai_enabled: bool = False
    openai_api_key: str = ""
    clear_api_key: bool = False


class TeacherAuthReq(BaseModel):
    password: str = ""


class TeacherSessionReq(BaseModel):
    session_token: str = ""


class TeacherPasswordSetReq(BaseModel):
    password: str = ""
    hint: str = ""
    current_password: str = ""


class TeacherPasswordRecoverReq(BaseModel):
    hint: str = ""


class FeedbackReq(BaseModel):
    session_token: str = ""
    teacher_comment: str = ""
    problem_def: int = 0
    data_collection: int = 0
    analysis: int = 0
    communication: int = 0


def require_teacher(password: str):
    if not verify_teacher_password(password):
        raise HTTPException(403, "invalid teacher password")


def create_teacher_session() -> str:
    now = datetime.now(timezone.utc)
    expired = [token for token, expires_at in teacher_sessions.items() if expires_at <= now]
    for token in expired:
        teacher_sessions.pop(token, None)
    token = secrets.token_urlsafe(32)
    teacher_sessions[token] = now + timedelta(hours=TEACHER_SESSION_HOURS)
    return token


def require_teacher_session(session_token: str):
    token = (session_token or "").strip()
    expires_at = teacher_sessions.get(token)
    if not expires_at or expires_at <= datetime.now(timezone.utc):
        teacher_sessions.pop(token, None)
        raise HTTPException(403, "invalid or expired teacher session")


def now_label() -> str:
    return datetime.now(KST).strftime("%Y-%m-%d %H:%M:%S")


def compact_text(value: str, limit: int = 80) -> str:
    text = " ".join((value or "").split())
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + "..."


def clamp_score(value: int) -> int:
    return max(0, min(5, int(value or 0)))


def add_feedback_total(row: dict) -> dict:
    row["total_score"] = sum(
        clamp_score(row.get(key, 0))
        for key in ["problem_def", "data_collection", "analysis", "communication"]
    )
    return row


def classroom_base_url() -> str:
    ip = os.getenv("AI_TAMGU_LAN_IP", "127.0.0.1")
    port = os.getenv("AI_TAMGU_PORT", "8000")
    return f"http://{ip}:{port}"


@app.get("/api/class-info")
def class_info():
    base = classroom_base_url()
    ai_settings = get_ai_settings_public()
    return {
        "base_url": base,
        "student_url": f"{base}/student.html",
        "teacher_url": f"{base}/teacher.html",
        "local_teacher_url": f"http://127.0.0.1:{os.getenv('AI_TAMGU_PORT', '8000')}/teacher.html",
        "class_url": f"{base}/class.html",
        "ai_mode_active": bool(ai_settings["online_ai_enabled"] and ai_settings["has_api_key"]),
        "has_api_key": ai_settings["has_api_key"],
    }


@app.post("/api/class-mode")
def set_class_mode(req: ClassModeReq, request: Request):
    client_host = request.client.host if request.client else ""
    if client_host not in {"127.0.0.1", "::1"}:
        raise HTTPException(403, "모드 전환은 교사 PC의 첫 화면에서만 가능합니다.")
    try:
        settings = set_ai_mode_enabled(req.enabled)
    except ValueError as exc:
        raise HTTPException(400, str(exc))
    except RuntimeError as exc:
        raise HTTPException(503, str(exc))
    return {
        "ok": True,
        "ai_mode_active": bool(settings["online_ai_enabled"] and settings["has_api_key"]),
        "has_api_key": settings["has_api_key"],
    }


@app.get("/api/qr.svg")
def qr_svg(text: str):
    value = (text or "").strip()
    if not value:
        raise HTTPException(400, "QR text is required")
    if len(value) > 500:
        raise HTTPException(400, "QR text is too long")
    image = qrcode.make(value, image_factory=qrcode.image.svg.SvgPathImage, box_size=12, border=2)
    output = io.BytesIO()
    image.save(output)
    return Response(output.getvalue(), media_type="image/svg+xml")


def summarize_progress(data: dict) -> str:
    parts = []
    labels = [
        ("계획", data.get("plan_note", "")),
        ("자료조사", data.get("guide_note", "")),
        ("설문", data.get("survey_note", "")),
        ("인터뷰", data.get("interview_note", "")),
        ("탐구일지", data.get("research_log", "")),
        ("보고서", data.get("report_note", "")),
    ]
    for label, value in labels:
        text = compact_text(value, 42)
        if text:
            parts.append(f"{label}: {text}")
    if parts:
        return " / ".join(parts[:3])
    if compact_text(data.get("report", ""), 70):
        return "보고서 초안을 생성했습니다."
    if compact_text(data.get("plan", ""), 70):
        return "탐구계획서를 확인하고 있습니다."
    return "아직 입력된 진행 상황이 없습니다."


def changed_update_text(before: dict, after: dict) -> str:
    fields = [
        ("계획서 메모", "plan_note"),
        ("자료조사 메모", "guide_note"),
        ("설문 메모", "survey_note"),
        ("인터뷰 메모", "interview_note"),
        ("탐구일지", "research_log"),
        ("보고서 정리 메모", "report_note"),
        ("보고서 초안", "report"),
    ]
    changes = []
    for label, key in fields:
        old = (before.get(key) or "").strip()
        new = (after.get(key) or "").strip()
        if new and new != old:
            changes.append(f"{label}: {compact_text(new, 90)}")
    if not changes:
        return "저장 버튼을 눌러 현재 내용을 다시 저장했습니다."
    return "\n".join(changes[:5])


def fetch_project_dict(cur, project_id: int) -> dict:
    cur.execute("SELECT * FROM projects WHERE id=?", (project_id,))
    row = cur.fetchone()
    return dict(row) if row else {}


def fetch_feedback_history(cur, project_id: int) -> list[dict]:
    cur.execute(
        """SELECT teacher_comment, problem_def, data_collection, analysis, communication, created_at
        FROM feedback
        WHERE project_id=? AND (teacher_comment<>'' OR problem_def>0 OR data_collection>0 OR analysis>0 OR communication>0)
        ORDER BY id DESC""",
        (project_id,),
    )
    return [add_feedback_total(dict(row)) for row in cur.fetchall()]


@app.on_event("startup")
def startup():
    init_db()


@app.post("/api/student/login")
def student_login(req: LoginReq):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT OR IGNORE INTO students(name, student_no) VALUES(?, ?)",
        (req.name.strip(), req.student_no.strip()),
    )
    conn.commit()
    cur.execute(
        "SELECT * FROM students WHERE name=? AND student_no=?",
        (req.name.strip(), req.student_no.strip()),
    )
    row = dict(cur.fetchone())
    conn.close()
    return row


@app.get("/api/student/{student_id}/projects")
def student_projects(student_id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM projects WHERE student_id=? ORDER BY updated_at DESC", (student_id,))
    rows = [dict(r) for r in cur.fetchall()]
    for row in rows:
        row["feedbacks"] = fetch_feedback_history(cur, row["id"])
    conn.close()
    return {"items": rows}


@app.post("/api/recommend")
def recommend(req: RecommendReq):
    return ai_engine.recommend(req.tag, req.detail)


@app.post("/api/projects")
def create_project(req: ProjectReq):
    if req.custom_topic:
        settings = get_ai_settings_public()
        if not (settings["online_ai_enabled"] and settings["has_api_key"]):
            raise HTTPException(403, "직접 주제 입력은 AI 모드에서만 사용할 수 있습니다.")
    plan_text = make_offline_plan(req.topic) if req.custom_topic else ai_engine.plan(req.topic)
    conn = get_conn()
    cur = conn.cursor()
    timestamp = now_label()
    cur.execute(
        """INSERT INTO projects(student_id, tag, interest, topic, subject, fit_score, plan, progress, updated_at)
        VALUES(?,?,?,?,?,?,?,?,?)""",
        (req.student_id, req.tag, req.interest, req.topic, req.subject, req.fit_score, plan_text, 30, timestamp),
    )
    project_id = cur.lastrowid
    cur.execute(
        "INSERT INTO project_updates(project_id, summary, changed_text, created_at) VALUES(?,?,?,?)",
        (project_id, "탐구 주제를 선택하고 계획서를 생성했습니다.", compact_text(plan_text, 160), timestamp),
    )
    conn.commit()
    conn.close()
    return {"project_id": project_id, "plan": plan_text}


@app.get("/api/projects/{project_id}")
def get_project(project_id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM projects WHERE id=?", (project_id,))
    row = cur.fetchone()
    if not row:
        conn.close()
        raise HTTPException(404, "project not found")
    data = dict(row)
    data["feedbacks"] = fetch_feedback_history(cur, project_id)
    conn.close()
    return data


@app.put("/api/projects/{project_id}")
def update_project(project_id: int, req: UpdateProjectReq):
    conn = get_conn()
    cur = conn.cursor()
    before = fetch_project_dict(cur, project_id)
    if not before:
        conn.close()
        raise HTTPException(404, "project not found")
    timestamp = now_label()
    after = {
        "plan": req.plan,
        "plan_note": req.plan_note,
        "guide_note": req.guide_note,
        "survey_note": req.survey_note,
        "interview_note": req.interview_note,
        "research_log": req.research_log,
        "progress_note": req.progress_note,
        "report": req.report,
        "report_note": req.report_note,
        "progress": req.progress,
    }
    summary = req.progress_note.strip() or summarize_progress(after)
    changed_text = changed_update_text(before, after)
    cur.execute(
        """UPDATE projects SET plan=?, plan_note=?, guide_note=?, survey_note=?, interview_note=?, research_log=?, progress_note=?, report=?, report_note=?, progress=?, updated_at=? WHERE id=?""",
        (
            req.plan,
            req.plan_note,
            req.guide_note,
            req.survey_note,
            req.interview_note,
            req.research_log,
            summary,
            req.report,
            req.report_note,
            req.progress,
            timestamp,
            project_id,
        ),
    )
    cur.execute(
        "INSERT INTO project_updates(project_id, summary, changed_text, created_at) VALUES(?,?,?,?)",
        (project_id, summary, changed_text, timestamp),
    )
    conn.commit()
    conn.close()
    return {"ok": True, "progress_note": summary, "updated_at": timestamp}


@app.put("/api/projects/{project_id}/progress-note")
def update_progress_note(project_id: int, req: ProgressNoteReq):
    conn = get_conn()
    cur = conn.cursor()
    timestamp = now_label()
    cur.execute(
        "UPDATE projects SET progress_note=?, updated_at=? WHERE id=?",
        (req.progress_note, timestamp, project_id),
    )
    if cur.rowcount == 0:
        conn.close()
        raise HTTPException(404, "project not found")
    cur.execute(
        "INSERT INTO project_updates(project_id, summary, changed_text, created_at) VALUES(?,?,?,?)",
        (project_id, req.progress_note or "진행 상황을 저장했습니다.", req.progress_note or "직접 입력한 진행 상황을 저장했습니다.", timestamp),
    )
    conn.commit()
    conn.close()
    return {"ok": True}


@app.delete("/api/projects/{project_id}")
def delete_project(project_id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id FROM projects WHERE id=?", (project_id,))
    if not cur.fetchone():
        conn.close()
        raise HTTPException(404, "project not found")
    cur.execute("DELETE FROM feedback WHERE project_id=?", (project_id,))
    cur.execute("DELETE FROM project_updates WHERE project_id=?", (project_id,))
    cur.execute("DELETE FROM projects WHERE id=?", (project_id,))
    conn.commit()
    conn.close()
    return {"ok": True}


@app.get("/api/projects/{project_id}/guide")
def get_guide(project_id: int):
    project = get_project(project_id)
    return {"items": ai_engine.guide(project["topic"])}


@app.get("/api/projects/{project_id}/survey")
def get_survey(project_id: int):
    project = get_project(project_id)
    return {"items": ai_engine.survey(project["topic"])}


@app.get("/api/projects/{project_id}/interview")
def get_interview(project_id: int):
    project = get_project(project_id)
    return {"items": ai_engine.interview(project["topic"])}


@app.post("/api/projects/{project_id}/report")
def generate_report(project_id: int):
    project = get_project(project_id)
    memo_text = "\n\n".join(
        text
        for text in [
            project.get("plan_note", ""),
            project.get("guide_note", ""),
            project.get("survey_note", ""),
            project.get("interview_note", ""),
            project.get("research_log", ""),
            project.get("report_note", ""),
        ]
        if text
    )
    report = ai_engine.report(project["topic"], project.get("plan", ""), memo_text)
    conn = get_conn()
    cur = conn.cursor()
    timestamp = now_label()
    cur.execute("UPDATE projects SET report=?, progress=?, progress_note=?, updated_at=? WHERE id=?", (report, 90, "보고서 초안을 생성했습니다.", timestamp, project_id))
    cur.execute(
        "INSERT INTO project_updates(project_id, summary, changed_text, created_at) VALUES(?,?,?,?)",
        (project_id, "보고서 초안을 생성했습니다.", compact_text(report, 160), timestamp),
    )
    conn.commit()
    conn.close()
    return {"report": report}


@app.post("/api/teacher/login")
def teacher_login(payload: dict):
    ok = verify_teacher_password(payload.get("password", ""))
    return {
        "ok": ok,
        "session_token": create_teacher_session() if ok else "",
        "expires_in_hours": TEACHER_SESSION_HOURS if ok else 0,
        **get_teacher_auth_public(),
    }


@app.get("/api/teacher/password-status")
def teacher_password_status():
    return get_teacher_auth_public()


@app.post("/api/teacher/password")
def set_teacher_password(req: TeacherPasswordSetReq):
    try:
        status = save_teacher_password(req.password, req.hint, req.current_password)
    except ValueError:
        raise HTTPException(400, "password is required")
    except PermissionError:
        raise HTTPException(403, "invalid teacher password")
    teacher_sessions.clear()
    return {"ok": True, **status}


@app.post("/api/teacher/password/recover")
def recover_password(req: TeacherPasswordRecoverReq):
    password = recover_teacher_password(req.hint)
    if not password:
        return {"ok": False}
    return {"ok": True, "password": password}


@app.post("/api/teacher/ai-settings")
def get_ai_settings(req: TeacherAuthReq):
    require_teacher(req.password)
    return get_ai_settings_public()


@app.post("/api/teacher/ai-settings/save")
def save_teacher_ai_settings(req: AiSettingsReq):
    require_teacher(req.password)
    try:
        settings = save_ai_settings(req.online_ai_enabled, req.openai_api_key, req.clear_api_key)
    except ValueError as exc:
        raise HTTPException(400, str(exc))
    except RuntimeError as exc:
        raise HTTPException(503, str(exc))
    return {"ok": True, "settings": settings}


@app.post("/api/teacher/ai-usage")
def teacher_ai_usage(req: TeacherAuthReq):
    require_teacher(req.password)
    return {**get_ai_usage_stats(), "cache": ai_engine.get_runtime_cache_stats()}


@app.post("/api/teacher/ai-usage/reset")
def teacher_ai_usage_reset(req: TeacherAuthReq):
    require_teacher(req.password)
    return {"ok": True, **reset_ai_usage_stats()}


@app.post("/api/teacher/dashboard")
def dashboard(req: TeacherSessionReq):
    require_teacher_session(req.session_token)
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """SELECT p.*, s.name, s.student_no,
        (SELECT teacher_comment FROM feedback f WHERE f.project_id=p.id ORDER BY f.created_at DESC LIMIT 1) AS teacher_comment
        FROM projects p JOIN students s ON p.student_id=s.id ORDER BY p.updated_at DESC"""
    )
    rows = [dict(r) for r in cur.fetchall()]
    for row in rows:
        computed_summary = summarize_progress(row)
        if not row.get("progress_note") or row.get("progress_note") == "아직 입력된 진행 상황이 없습니다.":
            row["progress_note"] = computed_summary
        cur.execute(
            "SELECT summary, changed_text, created_at FROM project_updates WHERE project_id=? ORDER BY id DESC LIMIT 5",
            (row["id"],),
        )
        row["updates"] = [dict(update) for update in cur.fetchall()]
        if not row["updates"] and computed_summary != "아직 입력된 진행 상황이 없습니다.":
            row["updates"] = [
                {
                    "summary": computed_summary,
                    "changed_text": changed_update_text({}, row),
                    "created_at": row.get("updated_at") or "저장 시간 기록 없음",
                }
            ]
        row["feedbacks"] = fetch_feedback_history(cur, row["id"])
    conn.close()
    return {"items": rows}


@app.post("/api/teacher/reset")
def reset_student_data(payload: dict):
    require_teacher(payload.get("password"))
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM feedback")
    cur.execute("DELETE FROM project_updates")
    cur.execute("DELETE FROM projects")
    cur.execute("DELETE FROM students")
    conn.commit()
    conn.close()
    return {"ok": True}


@app.post("/api/projects/{project_id}/feedback")
def save_feedback(project_id: int, req: FeedbackReq):
    require_teacher_session(req.session_token)
    conn = get_conn()
    cur = conn.cursor()
    timestamp = now_label()
    scores = {
        "problem_def": clamp_score(req.problem_def),
        "data_collection": clamp_score(req.data_collection),
        "analysis": clamp_score(req.analysis),
        "communication": clamp_score(req.communication),
    }
    cur.execute(
        """INSERT INTO feedback(project_id, teacher_comment, problem_def, data_collection, analysis, communication, created_at)
        VALUES(?,?,?,?,?,?,?)""",
        (
            project_id,
            req.teacher_comment,
            scores["problem_def"],
            scores["data_collection"],
            scores["analysis"],
            scores["communication"],
            timestamp,
        ),
    )
    conn.commit()
    conn.close()
    return {"ok": True, "created_at": timestamp, "total_score": sum(scores.values())}


app.mount("/", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="frontend")
