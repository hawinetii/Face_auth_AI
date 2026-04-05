# 🚀 FaceAuth AI – Face Recognition Login System

## 📌 Overview

**FaceAuth AI** is an AI-powered authentication system that allows users to register and log in using their face instead of traditional passwords.

This project demonstrates a complete **Machine Learning pipeline + Web Application**, combining computer vision, supervised learning, and an interactive user interface.

---

## 🎯 Features

* 📸 Face Registration (capture user images)
* 🔍 Face Detection using OpenCV
* 🧠 Face Recognition using KNN
* 🔐 Passwordless Login System
* 🖥️ Interactive UI using Streamlit
* ⚡ Real-time prediction via webcam

---

## 🧠 Technologies Used

* Python
* OpenCV (Computer Vision)
* NumPy (Data Processing)
* Scikit-learn (Machine Learning)
* Streamlit (Web UI)
* Git & GitHub (Collaboration)

---

## 🧩 Project Structure

```
faceauth-ai/
│
├── app/                        # Streamlit UI
│   └── main.py
│
├── data/
│   └── raw/                    # User face images (not included)
│
├── models/
│   └── face_model.pkl          # Trained model
│
├── src/                        # Core logic
│   ├── data_collection.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── train.py
│   └── predict.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/faceauth-ai.git
cd faceauth-ai
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Git Bash / Linux / Mac**

```bash
source venv/Scripts/activate
```

**Windows CMD**

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📸 Data Collection

Run:

```bash
python -m src.data_collection
```

* Capture 5–10 images per user
* Images stored in:

```
data/raw/<username>/
```

---

## 🧠 Model Training

Run:

```bash
python -m src.train
```

* Trains KNN model
* Saves model in:

```
models/face_model.pkl
```

---

## 🔐 Run the Application

```bash
streamlit run app/main.py
```

---

## 🖥️ How It Works

1. User registers their face
2. System captures and stores images
3. Images are processed and converted to features
4. ML model is trained on face data
5. During login:

   * Webcam captures image
   * Model predicts identity
   * Access is granted or denied

---

## 📊 Model Details

* Algorithm: K-Nearest Neighbors (KNN)
* Input: 64x64 grayscale images
* Feature: Flattened pixel array
* Decision: Based on distance threshold

---

## ⚠️ Notes

* Ensure proper lighting during face capture
* Minimum 2 users required for training

---

## 👥 Team Members

* Member 1 – Data Collection
* Member 2 – Preprocessing
* Member 3 – Machine Learning
* Member 4 – UI Development
* Member 5 – Integration & Testing

---

## 🚀 Future Improvements

* Deep Learning model (CNN)
* Face embedding (FaceNet)
* Database integration
* Mobile application
* Improved UI/UX

---

## 📄 License

This project is for academic purposes.

---



This project demonstrates the integration of AI and real-world applications, focusing on usability, simplicity, and security.

---
