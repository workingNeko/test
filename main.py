import streamlit as st
from auth import register_user, login_user

st.set_page_config(page_title="Login System", layout="centered")

st.title("🔐 Login System")

menu = ["Login", "Register"]
choice = st.sidebar.selectbox("Menu", menu)

# SESSION STATE
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# =====================
# LOGIN
# =====================
if choice == "Login":
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = login_user(username, password)

        if user:
            st.session_state.logged_in = True
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")

# =====================
# REGISTER
# =====================
elif choice == "Register":
    st.subheader("Create Account")

    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")

    if st.button("Register"):
        success = register_user(new_user, new_pass)

        if success:
            st.success("Account created!")
        else:
            st.error("Username already exists")

# =====================
# AFTER LOGIN
# =====================
if st.session_state.logged_in:
    st.write("🎉 Welcome! You are logged in.")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()