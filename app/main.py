import streamlit as st
from pages.register import register_page
from pages.login import login_page
from config import app_name

# ----------------- Page Config -----------------
st.set_page_config(page_title=app_name, layout="wide")

# ----------------- Hide default sidebar nav -----------------
st.markdown(
    """
    <style>
    [data-testid="stSidebarNav"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------- CSS Styling -----------------
st.markdown("""
<style>
/* Buttons */
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    height: 50px;
    width: 180px;
    font-size:16px;
    margin: 5px;
}
.stButton>button:hover {
    background-color: #45a049;
}

/* Input boxes */
div.stTextInput>div>input {
    height:40px;
    font-size:16px;
    border-radius: 8px;
    padding: 5px;
}

/* Image preview styling */
img {
    border-radius: 10px;
    margin: 5px;
    box-shadow: 2px 2px 5px grey;
}
</style>
""", unsafe_allow_html=True)


# ----------------- CSS Styling -----------------
st.markdown("""
<style>
/* ---------- Background & Fonts ---------- */
body {
    background: linear-gradient(to right, #f0f0f0, #e0e0ff);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* ---------- Buttons ---------- */
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 12px;
    height: 50px;
    width: 180px;
    font-size:16px;
    font-weight:bold;
    margin: 5px;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #45a049;
    transform: scale(1.05);
}

/* ---------- Input Boxes ---------- */
div.stTextInput>div>input {
    height:40px;
    font-size:16px;
    border-radius: 10px;
    padding: 5px;
}

/* ---------- Image Previews ---------- */
img {
    border-radius: 15px;
    margin: 5px;
    box-shadow: 4px 4px 12px grey;
    transition: transform 0.2s;
}
img:hover {
    transform: scale(1.05);
}

/* ---------- Sidebar ---------- */
.css-1d391kg {  /* sidebar background */
    background-color: #2c3e50;
    color: white;
}
.css-1d391kg h2, .css-1d391kg h3 {
    color: white;
}

/* ---------- Dark Mode Classes ---------- */
[data-theme="dark"] {
    background-color: #1e1e1e;
    color: #f0f0f0;
}
</style>
""", unsafe_allow_html=True)



# ----------------- App Title -----------------
st.title(app_name)

# ----------------- Sidebar Navigation -----------------
menu = ["Register", "Login"]
choice = st.sidebar.selectbox("Menu", menu)

# ----------------- Load selected page -----------------
if choice == "Register":
    register_page()
elif choice == "Login":
    login_page()