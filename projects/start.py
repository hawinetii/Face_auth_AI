import os
import streamlit as st
import numpy as np
import cv2

from src.train import train_model
from src.predict import predict_face

st.set_page_config(page_title="Face Auth AI", layout="centered")
st.title("📸 Face Recognition System")

choice = st.sidebar.selectbox("Menu", ["Register", "Login"])

DATA_PATH = "data"
os.makedirs(DATA_PATH, exist_ok=True)

# ---------------- REGISTER ----------------
if choice == "Register":
    st.header("Register New User")
    name = st.text_input("Enter Name")

    if "caps" not in st.session_state:
        st.session_state.caps = []

    img_file = st.camera_input("Capture Face")

    if img_file:
        st.session_state.caps.append(img_file)
        st.write(f"📸 Photos captured: {len(st.session_state.caps)}")

    for i, img in enumerate(st.session_state.caps):
        st.image(img, caption=f"Image {i+1}", width=200)

    if st.button("Clear Photos"):
        st.session_state.caps = []

    if st.button("Save & Train"):
        if name and len(st.session_state.caps) >= 5:
            user_dir = os.path.join(DATA_PATH, name)
            os.makedirs(user_dir, exist_ok=True)

            for i, f in enumerate(st.session_state.caps):
                with open(os.path.join(user_dir, f"img_{i}.jpg"), "wb") as img_out:
                    img_out.write(f.getbuffer())

            st.info("🤖 Training model...")
            train_model()

            st.success(f"✅ {name} registered successfully!")
            st.session_state.caps = []

        else:
            st.warning("⚠️ Enter name and capture at least 5 images")

# ---------------- LOGIN ----------------
elif choice == "Login":
    st.header("Face Login")

    img_file = st.camera_input("Look at the camera")

    if img_file and st.button("Login"):
        file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
        opencv_img = cv2.imdecode(file_bytes, 1)

        result = predict_face(opencv_img)

        if result == "Unknown":
            st.error("❌ Access Denied")
        elif "Error" in result or result == "No face detected":
            st.warning(result)
        else:
            st.success(f"✅ Welcome, {result}!")