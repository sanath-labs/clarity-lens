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


def clear_all_analyses() -> None:
    """
    Clears all records from the analyses table. Uses the same DB_PATH
    as the rest of this module (previously pointed at a different,
    unused database file due to a copy-paste bug).
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM analyses")
    conn.commit()
    conn.close()

def delete_analysis(analysis_id: int) -> None:
    """
    Deletes a single analysis record by its id.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM analyses WHERE id = ?", (analysis_id,))
    conn.commit()
    conn.close()

def search_analyses(keyword: str) -> list:
    """
    Returns all analyses whose input_text contains the given keyword
    (case-insensitive), most recent first.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, input_text, timestamp, flags_json, summary, steelman FROM analyses WHERE input_text LIKE ? ORDER BY timestamp DESC",
        ("%" + keyword + "%",)
    )
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

def delete_analysis(analysis_id: int) -> None:
    """
    Deletes a single analysis record by its id.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM analyses WHERE id = ?", (analysis_id,))
    conn.commit()
    conn.close()

def search_analyses(keyword: str) -> list:
    """
    Returns all analyses whose input_text contains the given keyword
    (case-insensitive), most recent first.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, input_text, timestamp, flags_json, summary, steelman FROM analyses WHERE input_text LIKE ? ORDER BY timestamp DESC",
        ("%" + keyword + "%",)
    )
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

def delete_analysis(analysis_id: int) -> None:
    """
    Deletes a single analysis record by its id.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM analyses WHERE id = ?", (analysis_id,))
    conn.commit()
    conn.close()

def search_analyses(keyword: str) -> list:
    """
    Returns all analyses whose input_text contains the given keyword
    (case-insensitive), most recent first.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, input_text, timestamp, flags_json, summary, steelman FROM analyses WHERE input_text LIKE ? ORDER BY timestamp DESC",
        ("%" + keyword + "%",)
    )
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

def delete_analysis(analysis_id: int) -> None:
    """
    Deletes a single analysis record by its id.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM analyses WHERE id = ?", (analysis_id,))
    conn.commit()
    conn.close()

def search_analyses(keyword: str) -> list:
    """
    Returns all analyses whose input_text contains the given keyword
    (case-insensitive), most recent first.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, input_text, timestamp, flags_json, summary, steelman FROM analyses WHERE input_text LIKE ? ORDER BY timestamp DESC",
        ("%" + keyword + "%",)
    )
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

def get_analyses_filtered(keyword: str = "", sort_order: str = "DESC") -> list:
    """
    Returns analyses filtered by an optional keyword and sorted by timestamp.
    sort_order must be either 'ASC' or 'DESC'.
    """
    order = "ASC" if sort_order.upper() == "ASC" else "DESC"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    if keyword.strip():
        query = f"SELECT id, input_text, timestamp, flags_json, summary, steelman FROM analyses WHERE input_text LIKE ? ORDER BY timestamp {order}"
        cursor.execute(query, ("%" + keyword.strip() + "%",))
    else:
        query = f"SELECT id, input_text, timestamp, flags_json, summary, steelman FROM analyses ORDER BY timestamp {order}"
        cursor.execute(query)
        
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
