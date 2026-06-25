import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
APP_DIR = Path(sys.executable).resolve().parent if getattr(sys, "frozen", False) else BASE_DIR
DATA_DIR = APP_DIR / "data"
DB_PATH = DATA_DIR / "inquiry_mate.db"


def get_conn():
    DATA_DIR.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def _columns(cur, table):
    cur.execute(f"PRAGMA table_info({table})")
    return {row[1] for row in cur.fetchall()}


def _add_column_if_missing(cur, table, column, definition):
    if column not in _columns(cur, table):
        cur.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")


def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        student_no TEXT NOT NULL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(name, student_no)
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        tag TEXT,
        interest TEXT,
        topic TEXT,
        subject TEXT,
        fit_score INTEGER DEFAULT 0,
        plan TEXT DEFAULT '',
        plan_note TEXT DEFAULT '',
        guide_note TEXT DEFAULT '',
        survey_note TEXT DEFAULT '',
        interview_note TEXT DEFAULT '',
        research_log TEXT DEFAULT '',
        progress_note TEXT DEFAULT '',
        report TEXT DEFAULT '',
        progress INTEGER DEFAULT 10,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(student_id) REFERENCES students(id)
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER NOT NULL,
        teacher_comment TEXT DEFAULT '',
        problem_def INTEGER DEFAULT 0,
        data_collection INTEGER DEFAULT 0,
        analysis INTEGER DEFAULT 0,
        communication INTEGER DEFAULT 0,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(project_id) REFERENCES projects(id)
    )
    """)
    _add_column_if_missing(cur, "projects", "progress_note", "TEXT DEFAULT ''")
    _add_column_if_missing(cur, "projects", "plan_note", "TEXT DEFAULT ''")
    _add_column_if_missing(cur, "projects", "guide_note", "TEXT DEFAULT ''")
    _add_column_if_missing(cur, "projects", "survey_note", "TEXT DEFAULT ''")
    _add_column_if_missing(cur, "projects", "interview_note", "TEXT DEFAULT ''")
    conn.commit()
    conn.close()
