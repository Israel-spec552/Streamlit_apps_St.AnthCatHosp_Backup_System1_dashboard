import streamlit as st
from auth import login, logout, get_current_user
from views import dashboard, manage_users, manage_departments, file_upload, audit_log, export_data
from db import init_db  # ✅ Import the DB initializer

# ✅ Initialize the database tables before anything else
init_db()

st.set_page_config(page_title="Department File Backup System", layout="wide")

user = get_current_user()

if user:
    st.sidebar.title("Navigation")
    menu = st.sidebar.radio("Go to", ["Dashboard", "Upload File", "Manage Users", "Manage Departments", "Audit Log", "Export Data", "Logout"])

    if menu == "Dashboard":
        dashboard.show(user)
    elif menu == "Upload File":
        file_upload.show(user)
    elif menu == "Manage Users" and user['role'] == 'chief_admin':
        manage_users.show()
    elif menu == "Manage Departments" and user['role'] == 'chief_admin':
        manage_departments.show()
    elif menu == "Audit Log":
        audit_log.show(user)
    elif menu == "Export Data":
        export_data.show(user)
    elif menu == "Logout":
        logout()
else:
    login()
