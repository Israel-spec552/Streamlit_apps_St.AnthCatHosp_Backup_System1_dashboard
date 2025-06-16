import streamlit as st
import pandas as pd
from db import get_connection

def show(user):
    st.title("Audit Log")
    conn = get_connection()
    query = """
    SELECT users.username, audit_log.action, audit_log.timestamp
    FROM audit_log
    JOIN users ON users.id = audit_log.user_id
    """
    if user["role"] != "chief_admin":
        query += " WHERE users.department_id=?"
        df = pd.read_sql(query, conn, params=(user["department_id"],))
    else:
        df = pd.read_sql(query, conn)
    st.dataframe(df)
    conn.close()
