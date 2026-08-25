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


def get_all_analyses() -> list:
    """
    Retrieves all saved analyses from the database, most recent first.
    Returns a list of dicts with keys: id, input_text, timestamp, flags,
    summary, steelman.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, input_text, timestamp, flags_json, summary, steelman FROM analyses ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()

    results = []
    for row in rows:
        results.append({
            "id": row[0],
            "input_text": row[1],
            "timestamp": row[2],
            "flags": json.loads(row[3]) if row[3] else [],
            "summary": row[4],
            "steelman": row[5],
        })
    return results
