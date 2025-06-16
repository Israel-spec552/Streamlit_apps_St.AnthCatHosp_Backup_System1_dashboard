import streamlit as st
from db import get_connection

def show(user):
    st.title("Upload File")
    uploaded_file = st.file_uploader("Choose file")
    if uploaded_file:
        file_bytes = uploaded_file.read()
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO files (filename, content, uploaded_by, department_id) VALUES (?, ?, ?, ?)",
            (uploaded_file.name, file_bytes, user["id"], user["department_id"])
        )
        cursor.execute("INSERT INTO audit_log (user_id, action) VALUES (?, ?)", (user["id"], "upload_file"))
        conn.commit()
        conn.close()
        st.success("File uploaded successfully")
