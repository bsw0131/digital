import sys
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import ai_engine
from database import get_conn, init_db

BASE_DIR = Path(__file__).resolve().parent.parent
RESOURCE_DIR = Path(getattr(sys, "_MEIPASS", BASE_DIR))
FRONTEND_DIR = RESOURCE_DIR / "frontend"
TEACHER_PASSWORD = "teacher1234"

app = FastAPI(title="AI 탐구메이트")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


class LoginReq(BaseModel):
    name: str
    student_no: str


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


class UpdateProjectReq(BaseModel):
    plan: str = ""
    plan_note: str = ""
    guide_note: str = ""
    survey_note: str = ""
    interview_note: str = ""
    research_log: str = ""
    progress_note: str = ""
    report: str = ""
    progress: int = 10


class ProgressNoteReq(BaseModel):
    progress_note: str = ""


class FeedbackReq(BaseModel):
    teacher_comment: str = ""
    problem_def: int = 0
    data_collection: int = 0
    analysis: int = 0
    communication: int = 0


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
    conn.close()
    return {"items": rows}


@app.post("/api/recommend")
def recommend(req: RecommendReq):
    return ai_engine.recommend(req.tag, req.detail)


@app.post("/api/projects")
def create_project(req: ProjectReq):
    plan_text = ai_engine.plan(req.topic)
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """INSERT INTO projects(student_id, tag, interest, topic, subject, fit_score, plan, progress)
        VALUES(?,?,?,?,?,?,?,?)""",
        (req.student_id, req.tag, req.interest, req.topic, req.subject, req.fit_score, plan_text, 30),
    )
    conn.commit()
    project_id = cur.lastrowid
    conn.close()
    return {"project_id": project_id, "plan": plan_text}


@app.get("/api/projects/{project_id}")
def get_project(project_id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM projects WHERE id=?", (project_id,))
    row = cur.fetchone()
    conn.close()
    if not row:
        raise HTTPException(404, "project not found")
    return dict(row)


@app.put("/api/projects/{project_id}")
def update_project(project_id: int, req: UpdateProjectReq):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """UPDATE projects SET plan=?, plan_note=?, guide_note=?, survey_note=?, interview_note=?, research_log=?, progress_note=?, report=?, progress=?, updated_at=CURRENT_TIMESTAMP WHERE id=?""",
        (
            req.plan,
            req.plan_note,
            req.guide_note,
            req.survey_note,
            req.interview_note,
            req.research_log,
            req.progress_note,
            req.report,
            req.progress,
            project_id,
        ),
    )
    conn.commit()
    conn.close()
    return {"ok": True}


@app.put("/api/projects/{project_id}/progress-note")
def update_progress_note(project_id: int, req: ProgressNoteReq):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "UPDATE projects SET progress_note=?, updated_at=CURRENT_TIMESTAMP WHERE id=?",
        (req.progress_note, project_id),
    )
    if cur.rowcount == 0:
        conn.close()
        raise HTTPException(404, "project not found")
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
        ]
        if text
    )
    report = ai_engine.report(project["topic"], project.get("plan", ""), memo_text)
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE projects SET report=?, progress=?, updated_at=CURRENT_TIMESTAMP WHERE id=?", (report, 90, project_id))
    conn.commit()
    conn.close()
    return {"report": report}


@app.post("/api/teacher/login")
def teacher_login(payload: dict):
    return {"ok": payload.get("password") == TEACHER_PASSWORD}


@app.get("/api/teacher/dashboard")
def dashboard():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """SELECT p.*, s.name, s.student_no,
        (SELECT teacher_comment FROM feedback f WHERE f.project_id=p.id ORDER BY f.created_at DESC LIMIT 1) AS teacher_comment
        FROM projects p JOIN students s ON p.student_id=s.id ORDER BY p.updated_at DESC"""
    )
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return {"items": rows}


@app.post("/api/teacher/reset")
def reset_student_data(payload: dict):
    if payload.get("password") != TEACHER_PASSWORD:
        raise HTTPException(403, "invalid teacher password")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM feedback")
    cur.execute("DELETE FROM projects")
    cur.execute("DELETE FROM students")
    conn.commit()
    conn.close()
    return {"ok": True}


@app.post("/api/projects/{project_id}/feedback")
def save_feedback(project_id: int, req: FeedbackReq):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """INSERT INTO feedback(project_id, teacher_comment, problem_def, data_collection, analysis, communication)
        VALUES(?,?,?,?,?,?)""",
        (project_id, req.teacher_comment, req.problem_def, req.data_collection, req.analysis, req.communication),
    )
    conn.commit()
    conn.close()
    return {"ok": True}


app.mount("/", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="frontend")