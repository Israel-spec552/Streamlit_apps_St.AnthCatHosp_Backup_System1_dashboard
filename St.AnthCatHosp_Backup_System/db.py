import sqlite3
from models import create_tables
import hashlib

DB_PATH = "database.db"

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_db():
    conn = get_connection()
    create_tables(conn)  # Create tables using models.py
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

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_default_admin():
    conn = get_connection()
    cursor = conn.cursor()

    # Check if a chief_admin already exists
    cursor.execute("SELECT COUNT(*) FROM users WHERE role = 'chief_admin'")
    if cursor.fetchone()[0] == 0:
        # Insert default department if not exists
        cursor.execute("INSERT OR IGNORE INTO departments (id, name) VALUES (?, ?)", (1, "Administration"))

        # Insert default admin user
        cursor.execute("""
            INSERT INTO users (username, password, role, department_id)
            VALUES (?, ?, ?, ?)
        """, ("admin", hash_password("admin123"), "chief_admin", 1))

        conn.commit()

    conn.close()
