import streamlit as st
from db import init_db
from db import create_default_admin
from auth import login, logout, get_current_user
from views import (
    dashboard,
    manage_users,
    manage_departments,
    file_upload,
    audit_log,
    export_data
)

# Initialize database
init_db()
create_default_admin()

st.set_page_config(page_title="Department File Backup System", layout="wide")

def render_sidebar(user):
    st.sidebar.title(f"Welcome, {user['username']} ({user['role']})")
    menu_options = ["Dashboard", "Upload File"]

    if user["role"] == "chief_admin":
        menu_options += ["Manage Users", "Manage Departments", "Audit Log", "Export Data"]
    elif user["role"] == "department_admin":
        menu_options += ["Manage Users", "Audit Log"]

    menu_options.append("Logout")
    return st.sidebar.radio("Go to", menu_options)

def main():
    user = get_current_user()  # ✅ Get the user dynamically inside main()

    if not user:
        login()  # Show login form
        return

    # Sidebar and navigation
    selected_page = render_sidebar(user)

    if selected_page == "Dashboard":
        dashboard.show(user)
    elif selected_page == "Upload File":
        file_upload.show(user)
    elif selected_page == "Manage Users" and user["role"] == "chief_admin":
        manage_users.show()
    elif selected_page == "Manage Departments" and user["role"] == "chief_admin":
        manage_departments.show()
    elif selected_page == "Audit Log":
        audit_log.show(user)
    elif selected_page == "Export Data":
        export_data.show(user)
    elif selected_page == "Logout":
        logout()
        st.experimental_rerun()

if __name__ == "__main__":
    main()
