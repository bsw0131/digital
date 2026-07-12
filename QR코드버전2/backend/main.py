import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import ai_engine
from database import get_conn, init_db
from settings_store import get_ai_settings_public, save_ai_settings

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"
TEACHER_PASSWORD = "teacher1234"
KST = timezone(timedelta(hours=9))

app = FastAPI(title="AI 탐구메이트 QR코드버전2")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


class LoginReq(BaseModel):
    name: str
    student_no: str


class RecommendReq(BaseModel):
    tag: str = ""
    detail: str = ""


class ProjectReq(BaseModel):
    student_id: int
    tag: str = ""
    interest: str = ""
    topic: str
    subject: str = ""
    fit_score: int = 0


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


class FeedbackReq(BaseModel):
    teacher_comment: str = ""
    problem_def: int = 0
    data_collection: int = 0
    analysis: int = 0
    communication: int = 0


class TeacherAuthReq(BaseModel):
    password: str = ""


class AiSettingsReq(BaseModel):
    password: str = ""
    online_ai_enabled: bool = False
    openai_api_key: str = ""
    clear_api_key: bool = False
    model: str = "gpt-4o-mini"


def now_label():
    return datetime.now(KST).strftime("%Y-%m-%d %H:%M:%S")


def require_teacher(password):
    if password != TEACHER_PASSWORD:
        raise HTTPException(403, "invalid teacher password")


def compact_text(value, limit=80):
    text = " ".join((value or "").split())
    return text if len(text) <= limit else text[:limit].rstrip() + "..."


def summarize_progress(data):
    labels = [("계획", "plan_note"), ("자료조사", "guide_note"), ("설문", "survey_note"), ("인터뷰", "interview_note"), ("탐구일지", "research_log"), ("보고서", "report_note")]
    parts = [f"{label}: {compact_text(data.get(key), 42)}" for label, key in labels if compact_text(data.get(key), 42)]
    if parts:
        return " / ".join(parts[:3])
    if compact_text(data.get("report")):
        return "보고서 초안을 생성했습니다."
    if compact_text(data.get("plan")):
        return "탐구계획서를 확인하고 있습니다."
    return "아직 입력된 진행 상황이 없습니다."


def changed_text(before, after):
    fields = [("계획서 메모", "plan_note"), ("자료조사 메모", "guide_note"), ("설문 메모", "survey_note"), ("인터뷰 메모", "interview_note"), ("탐구일지", "research_log"), ("보고서 메모", "report_note")]
    changes = []
    for label, key in fields:
        old = (before.get(key) or "").strip()
        new = (after.get(key) or "").strip()
        if new and new != old:
            changes.append(f"{label}: {compact_text(new, 90)}")
    return "\n".join(changes[:5]) or "현재 내용을 다시 저장했습니다."


def fetch_project(cur, project_id):
    cur.execute("SELECT * FROM projects WHERE id=?", (project_id,))
    row = cur.fetchone()
    return dict(row) if row else {}


def feedbacks(cur, project_id):
    cur.execute("SELECT teacher_comment, problem_def, data_collection, analysis, communication, created_at FROM feedback WHERE project_id=? ORDER BY id DESC", (project_id,))
    rows = []
    for row in cur.fetchall():
        item = dict(row)
        item["total_score"] = sum(int(item.get(k) or 0) for k in ["problem_def", "data_collection", "analysis", "communication"])
        rows.append(item)
    return rows


@app.on_event("startup")
def startup():
    init_db()


@app.post("/api/student/login")
def student_login(req: LoginReq):
    conn = get_conn(); cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO students(name, student_no) VALUES(?,?)", (req.name.strip(), req.student_no.strip()))
    conn.commit()
    cur.execute("SELECT * FROM students WHERE name=? AND student_no=?", (req.name.strip(), req.student_no.strip()))
    row = dict(cur.fetchone())
    conn.close()
    return row


@app.get("/api/student/{student_id}/projects")
def student_projects(student_id: int):
    conn = get_conn(); cur = conn.cursor()
    cur.execute("SELECT * FROM projects WHERE student_id=? ORDER BY updated_at DESC", (student_id,))
    rows = [dict(r) for r in cur.fetchall()]
    for row in rows:
        row["feedbacks"] = feedbacks(cur, row["id"])
    conn.close()
    return {"items": rows}


@app.post("/api/recommend")
def recommend(req: RecommendReq):
    return ai_engine.recommend(req.tag, req.detail)


@app.post("/api/projects")
def create_project(req: ProjectReq):
    plan_text = ai_engine.plan(req.topic)
    ts = now_label()
    conn = get_conn(); cur = conn.cursor()
    cur.execute("INSERT INTO projects(student_id, tag, interest, topic, subject, fit_score, plan, progress, updated_at) VALUES(?,?,?,?,?,?,?,?,?)", (req.student_id, req.tag, req.interest, req.topic, req.subject, req.fit_score, plan_text, 30, ts))
    project_id = cur.lastrowid
    cur.execute("INSERT INTO project_updates(project_id, summary, changed_text, created_at) VALUES(?,?,?,?)", (project_id, "탐구 주제를 선택하고 계획서를 생성했습니다.", compact_text(plan_text, 160), ts))
    conn.commit(); conn.close()
    return {"project_id": project_id, "plan": plan_text}


@app.get("/api/projects/{project_id}")
def get_project(project_id: int):
    conn = get_conn(); cur = conn.cursor()
    row = fetch_project(cur, project_id)
    if not row:
        conn.close(); raise HTTPException(404, "project not found")
    row["feedbacks"] = feedbacks(cur, project_id)
    conn.close()
    return row


@app.put("/api/projects/{project_id}")
def update_project(project_id: int, req: UpdateProjectReq):
    conn = get_conn(); cur = conn.cursor()
    before = fetch_project(cur, project_id)
    if not before:
        conn.close(); raise HTTPException(404, "project not found")
    after = req.dict()
    summary = req.progress_note.strip() or summarize_progress(after)
    ts = now_label()
    cur.execute("UPDATE projects SET plan=?, plan_note=?, guide_note=?, survey_note=?, interview_note=?, research_log=?, progress_note=?, report=?, report_note=?, progress=?, updated_at=? WHERE id=?", (req.plan, req.plan_note, req.guide_note, req.survey_note, req.interview_note, req.research_log, summary, req.report, req.report_note, req.progress, ts, project_id))
    cur.execute("INSERT INTO project_updates(project_id, summary, changed_text, created_at) VALUES(?,?,?,?)", (project_id, summary, changed_text(before, after), ts))
    conn.commit(); conn.close()
    return {"ok": True, "updated_at": ts}


@app.put("/api/projects/{project_id}/progress-note")
def update_progress_note(project_id: int, req: ProgressNoteReq):
    ts = now_label()
    conn = get_conn(); cur = conn.cursor()
    cur.execute("UPDATE projects SET progress_note=?, updated_at=? WHERE id=?", (req.progress_note, ts, project_id))
    if cur.rowcount == 0:
        conn.close(); raise HTTPException(404, "project not found")
    cur.execute("INSERT INTO project_updates(project_id, summary, changed_text, created_at) VALUES(?,?,?,?)", (project_id, req.progress_note or "진행 상황을 저장했습니다.", req.progress_note or "직접 입력한 진행 상황을 저장했습니다.", ts))
    conn.commit(); conn.close()
    return {"ok": True}


@app.delete("/api/projects/{project_id}")
def delete_project(project_id: int):
    conn = get_conn(); cur = conn.cursor()
    cur.execute("DELETE FROM feedback WHERE project_id=?", (project_id,))
    cur.execute("DELETE FROM project_updates WHERE project_id=?", (project_id,))
    cur.execute("DELETE FROM projects WHERE id=?", (project_id,))
    conn.commit(); conn.close()
    return {"ok": True}


@app.get("/api/projects/{project_id}/guide")
def get_guide(project_id: int):
    return {"items": ai_engine.guide(get_project(project_id)["topic"])}


@app.get("/api/projects/{project_id}/survey")
def get_survey(project_id: int):
    return {"items": ai_engine.survey(get_project(project_id)["topic"])}


@app.get("/api/projects/{project_id}/interview")
def get_interview(project_id: int):
    return {"items": ai_engine.interview(get_project(project_id)["topic"])}


@app.post("/api/projects/{project_id}/report")
def make_report(project_id: int):
    project = get_project(project_id)
    memo = "\n\n".join([project.get("plan_note", ""), project.get("guide_note", ""), project.get("survey_note", ""), project.get("interview_note", ""), project.get("research_log", ""), project.get("report_note", "")])
    report = ai_engine.report(project["topic"], project.get("plan", ""), memo)
    ts = now_label(); conn = get_conn(); cur = conn.cursor()
    cur.execute("UPDATE projects SET report=?, progress=?, progress_note=?, updated_at=? WHERE id=?", (report, 90, "보고서 초안을 생성했습니다.", ts, project_id))
    cur.execute("INSERT INTO project_updates(project_id, summary, changed_text, created_at) VALUES(?,?,?,?)", (project_id, "보고서 초안을 생성했습니다.", compact_text(report, 160), ts))
    conn.commit(); conn.close()
    return {"report": report}


@app.post("/api/teacher/login")
def teacher_login(payload: dict):
    return {"ok": payload.get("password") == TEACHER_PASSWORD}


@app.get("/api/teacher/dashboard")
def dashboard():
    conn = get_conn(); cur = conn.cursor()
    cur.execute("SELECT p.*, s.name, s.student_no, (SELECT teacher_comment FROM feedback f WHERE f.project_id=p.id ORDER BY f.created_at DESC LIMIT 1) AS teacher_comment FROM projects p JOIN students s ON p.student_id=s.id ORDER BY p.updated_at DESC")
    rows = [dict(r) for r in cur.fetchall()]
    for row in rows:
        if not row.get("progress_note"):
            row["progress_note"] = summarize_progress(row)
        cur.execute("SELECT summary, changed_text, created_at FROM project_updates WHERE project_id=? ORDER BY id DESC LIMIT 5", (row["id"],))
        row["updates"] = [dict(u) for u in cur.fetchall()]
        row["feedbacks"] = feedbacks(cur, row["id"])
    conn.close()
    return {"items": rows}


@app.post("/api/projects/{project_id}/feedback")
def save_feedback(project_id: int, req: FeedbackReq):
    ts = now_label(); conn = get_conn(); cur = conn.cursor()
    cur.execute("INSERT INTO feedback(project_id, teacher_comment, problem_def, data_collection, analysis, communication, created_at) VALUES(?,?,?,?,?,?,?)", (project_id, req.teacher_comment, req.problem_def, req.data_collection, req.analysis, req.communication, ts))
    conn.commit(); conn.close()
    return {"ok": True, "created_at": ts}


@app.post("/api/teacher/reset")
def reset(payload: dict):
    require_teacher(payload.get("password"))
    conn = get_conn(); cur = conn.cursor()
    for table in ["feedback", "project_updates", "projects", "students"]:
        cur.execute(f"DELETE FROM {table}")
    conn.commit(); conn.close()
    return {"ok": True}


@app.post("/api/teacher/ai-settings")
def ai_settings(req: TeacherAuthReq):
    require_teacher(req.password)
    return get_ai_settings_public()


@app.post("/api/teacher/ai-settings/save")
def save_settings(req: AiSettingsReq):
    require_teacher(req.password)
    return {"ok": True, "settings": save_ai_settings(req.online_ai_enabled, req.openai_api_key, req.clear_api_key, req.model)}


app.mount("/", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="frontend")
