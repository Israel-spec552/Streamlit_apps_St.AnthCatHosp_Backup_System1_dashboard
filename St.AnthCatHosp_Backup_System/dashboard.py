import streamlit as st
from db import get_connection
import pandas as pd

def show(user):
    st.title("Dashboard")
    conn = get_connection()
    cursor = conn.cursor()

    if user["role"] == "chief_admin":
        cursor.execute("SELECT id, filename, timestamp FROM files")
    else:
        cursor.execute("SELECT id, filename, timestamp FROM files WHERE department_id=?", (user["department_id"],))

    files = cursor.fetchall()

    st.write("Uploaded Files:")
    for file_id, filename, timestamp in files:
        st.write(f"**{filename}** - *{timestamp}*")
        with st.form(f"form_{file_id}"):
            if st.form_submit_button("Download"):
                cursor.execute("SELECT content FROM files WHERE id=?", (file_id,))
                result = cursor.fetchone()
                if result:
                    content = result[0]
                    st.download_button("Click to Download", content, file_name=filename)
                else:
                    st.warning("File not found in database.")

    conn.close()
