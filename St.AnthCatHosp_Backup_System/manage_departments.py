import streamlit as st
from db import get_connection

def show():
    st.title("Manage Departments")
    conn = get_connection()
    cursor = conn.cursor()

    dept_name = st.text_input("New Department Name")
    if st.button("Add Department"):
        cursor.execute("INSERT INTO departments (name) VALUES (?)", (dept_name,))
        conn.commit()
        st.success("Department added")

    st.write("Existing Departments:")
    departments = cursor.execute("SELECT name FROM departments").fetchall()
    st.table(departments)
    conn.close()
