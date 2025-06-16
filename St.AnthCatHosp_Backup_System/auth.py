import streamlit as st
from db import get_user_by_username

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = get_user_by_username(username)
        if user and user["password"] == password:
            st.session_state.user = user
            st.rerun()
        else:
            st.error("Invalid credentials")

def logout():
    st.session_state.user = None
    st.success("Logged out successfully")
    st.rerun()

def get_current_user():
    return st.session_state.get("user", None)
