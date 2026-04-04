import streamlit as st
import os
from PIL import Image

st.title("Face Recognition System")

menu = ["Register", "Login"]
choice = st.sidebar.selectbox("Menu", menu)

DATA_PATH = "data"

# Create data folder if not exists
if not os.path.exists(DATA_PATH):
    os.makedirs(DATA_PATH)

# ---------------- REGISTER PAGE ----------------
if choice == "Register":
    st.header("Register User")

    name = st.text_input("Enter your name")

    img_file = st.camera_input("Capture your face")

    if img_file is not None:
        st.image(img_file)

        if st.button("Save"):
            if name == "":
                st.warning("Please enter a name")
            else:
                user_folder = os.path.join(DATA_PATH, name)

                if not os.path.exists(user_folder):
                    os.makedirs(user_folder)

                file_path = os.path.join(user_folder, "image.jpg")

                with open(file_path, "wb") as f:
                    f.write(img_file.getbuffer())

                st.success(f"{name} registered successfully!")

# ---------------- LOGIN PAGE ----------------
elif choice == "Login":
    st.header("Login")

    img_file = st.camera_input("Capture your face")

    if img_file is not None:
        st.image(img_file)

        if st.button("Login"):
            # Placeholder logic
            users = os.listdir(DATA_PATH)

            if len(users) == 0:
                st.error("No users registered")
            else:
                st.success("Face detected!")
                st.info("Matching logic will be added here")