import streamlit as st
from pages.register import register_page
from pages.login import login_page
from config import app_name

# Browser tab title
st.markdown(
    """
    <style>
    [data-testid="stSidebarNav"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True
)
st.set_page_config(page_title=app_name)

# Main title
st.title(app_name)

# Sidebar menu
menu = ["Register", "Login"]
choice = st.sidebar.selectbox("Menu", menu)

# Load the selected page
if choice == "Register":
    register_page()
elif choice == "Login":
    login_page()