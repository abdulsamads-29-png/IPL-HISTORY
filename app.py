import streamlit as st

st.set_page_config(
    page_title="IPL Analytics",
    page_icon="🏏",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("IPL Analytics")
    st.subheader("Login / Sign In")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.switch_page("pages/1_About_Project.py")
        else:
            st.error("Invalid username or password.")
else:
    st.title("IPL Analytics")
    st.write("You are already logged in.")
    if st.button("Go to About Project"):
        st.switch_page("pages/1_About_Project.py")
