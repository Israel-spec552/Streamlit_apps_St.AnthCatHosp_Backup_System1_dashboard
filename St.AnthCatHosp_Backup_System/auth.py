import streamlit as st
from db import get_user_by_username
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password, hashed):
    return hash_password(password) == hashed

def login():
    st.title("🔐 Login")

    if "user" not in st.session_state:
        st.session_state.user = None

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            user = get_user_by_username(username)
            if user and verify_password(password, user["password"]):
                st.session_state.user = user
                st.success(f"Welcome, {user['username']}!")
                st.experimental_rerun()
            else:
                st.error("❌ Invalid username or password.")

def logout():
    if "user" in st.session_state:
        del st.session_state.user
    st.success("You have been logged out.")
    st.experimental_rerun()

def get_current_user():
    return st.session_state.get("user", None)
