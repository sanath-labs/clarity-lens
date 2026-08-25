import sqlite3
import json
from datetime import datetime

DB_PATH = "clarity_lens.db"


def init_db():
    """
    Creates the analyses table if it does not already exist.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            input_text TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            flags_json TEXT,
            summary TEXT,
            steelman TEXT
        )
    """)
    conn.commit()
    conn.close()


def save_analysis(input_text: str, flags: list, summary: str, steelman: str) -> None:
    """
    Saves a completed analysis (input text, per-sentence flags, LLM summary,
    and LLM steelman argument) to the database with a timestamp.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO analyses (input_text, timestamp, flags_json, summary, steelman) VALUES (?, ?, ?, ?, ?)",
        (input_text, datetime.now().isoformat(), json.dumps(flags), summary, steelman)
    )
    conn.commit()
    conn.close()
