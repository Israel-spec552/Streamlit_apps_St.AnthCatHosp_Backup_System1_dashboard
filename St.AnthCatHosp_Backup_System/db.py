import sqlite3
from models import create_tables  # This should be a Python function, not raw SQL
import hashlib

DB_PATH = "database.db"

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_db():
    conn = get_connection()
    create_tables(conn)  # Pass connection to models.py
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

def create_default_admin():
    conn = get_connection()
    cursor = conn.cursor()

    # Check if admin user exists
    cursor.execute("SELECT * FROM users WHERE username = ?", ("admin",))
    if cursor.fetchone():
        conn.close()
        return

    # Insert default department (id=1)
    cursor.execute("INSERT OR IGNORE INTO departments (id, name) VALUES (?, ?)", (1, "Administration"))

    # Create hashed password
    password = "admin123"
    hashed = hashlib.sha256(password.encode()).hexdigest()

    # Insert default admin
    cursor.execute("""
        INSERT INTO users (username, password, role, department_id)
        VALUES (?, ?, ?, ?)
    """, ("admin", hashed, "chief_admin", 1))

    conn.commit()
    conn.close()
