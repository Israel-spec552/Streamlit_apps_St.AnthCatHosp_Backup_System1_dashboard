import streamlit as st
from db import get_connection

def show():
    st.title("Manage Users")
    conn = get_connection()
    cursor = conn.cursor()

    username = st.text_input("New Username")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["chief_admin", "department_admin", "user"])
    departments = cursor.execute("SELECT id, name FROM departments").fetchall()
    department = st.selectbox("Department", departments, format_func=lambda x: x[1])

    if st.button("Add User"):
        cursor.execute("INSERT INTO users (username, password, role, department_id) VALUES (?, ?, ?, ?)",
                       (username, password, role, department[0]))
        conn.commit()
        st.success("User added")

    st.write("Existing Users:")
    users = cursor.execute("SELECT username, role FROM users").fetchall()
    st.table(users)
    conn.close()
