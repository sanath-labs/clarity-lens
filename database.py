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
