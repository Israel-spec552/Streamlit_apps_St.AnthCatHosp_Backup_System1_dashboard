import streamlit as st
import pandas as pd
from db import get_connection

def show(user):
    st.title("Export Data")
    conn = get_connection()

    query = "SELECT filename, timestamp FROM files"
    if user["role"] != "chief_admin":
        query += " WHERE department_id=?"
        df = pd.read_sql(query, conn, params=(user["department_id"],))
    else:
        df = pd.read_sql(query, conn)

    file_format = st.selectbox("Export Format", ["CSV", "Excel"])
    if st.button("Export"):
        if file_format == "CSV":
            st.download_button("Download CSV", df.to_csv(index=False), "export.csv", "text/csv")
        else:
            from io import BytesIO
            output = BytesIO()
            df.to_excel(output, index=False)
            st.download_button("Download Excel", output.getvalue(), "export.xlsx", "application/vnd.ms-excel")
    conn.close()
