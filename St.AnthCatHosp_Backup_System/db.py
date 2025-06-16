import sqlite3
from models import create_tables  # Import the function from models.py

DB_PATH = "database.db"

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_db():
    create_tables()  # Call the Python function that creates tables

def get_user_by_username(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(zip(["id", "username", "password", "role", "department_id"], row))
    return None
