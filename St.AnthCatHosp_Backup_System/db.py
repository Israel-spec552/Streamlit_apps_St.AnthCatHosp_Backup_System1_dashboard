import sqlite3
from pathlib import Path

DB_PATH = "database.db"

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executescript(Path("models.py").read_text())
    conn.commit()
    conn.close()

def get_user_by_username(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(zip(["id", "username", "password", "role", "department_id"], row))
    return None
