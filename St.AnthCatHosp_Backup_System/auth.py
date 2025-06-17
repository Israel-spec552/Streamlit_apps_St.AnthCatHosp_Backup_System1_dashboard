import streamlit as st
from db import get_user_by_username
import hashlib

def login():
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = get_user_by_username(username)
        if user and verify_password(password, user["password"]):
            st.session_state.user = user
            st.success(f"Welcome, {user['username']}!")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password.")

def logout():
    if "user" in st.session_state:
        del st.session_state.user

def get_current_user():
    return st.session_state.get("user")

def verify_password(password, hashed):
    return hashlib.sha256(password.encode()).hexdigest() == hashed
