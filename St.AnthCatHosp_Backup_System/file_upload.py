import streamlit as st
from db import get_connection

def show(user):
    st.title("Upload File")  # ⬅️ Must have something to show
    uploaded_file = st.file_uploader("Choose file")

    if uploaded_file:
        content = uploaded_file.read()
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO files (filename, content, uploaded_by, department_id) VALUES (?, ?, ?, ?)",
            (uploaded_file.name, content, user["id"], user["department_id"])
        )
        conn.commit()
        st.success("File uploaded successfully.")
        conn.close()
