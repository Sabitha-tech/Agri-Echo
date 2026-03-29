# 🌿 AgriEcho – AI Crop Disease Detection System

## 📌 Overview
AgriEcho is an AI-powered web application that helps farmers detect crop diseases using image analysis. It provides multilingual support (English, Tamil, Hindi) along with voice assistance, making it easy for farmers to understand results.

---

## 🎯 Problem Statement
Farmers often struggle to identify crop diseases early, which leads to reduced yield and financial loss. Access to experts is limited, especially in rural areas.

---

## 💡 Solution
AgriEcho uses a trained machine learning model to analyze crop images and detect diseases. It provides simple solutions in multiple languages with voice output support.

---

## ✨ Features
- 📸 Upload crop image for disease detection
- 🤖 AI-based prediction using TensorFlow model
- 🌍 Multilingual support (English, Tamil, Hindi)
- 🔊 Voice output for better understanding
- 👤 User authentication (Login/Register)
- 📊 Dashboard with disease analytics
- 🗂️ Crop history tracking
- 🌐 Works in low or no internet environments

---

## 🛠️ Tech Stack
- Backend: Flask (Python)
- Machine Learning: TensorFlow / Keras
- Frontend: HTML, CSS, JavaScript
- Database: SQLite

---


## 📂 Project Structure

agri-echo/
│
├── backend/
│ ├── app.py
│ ├── agri.db
│ ├── my_model.keras
│ ├── templates/
│ │ ├── login.html
│ │ ├── signup.html
│ │ ├── index.html
│ │ ├── profile.html
│ │ └── dashboard.html

---

## 🚀 How to Run

### 1. Clone Repository

git clone https://github.com/Sabitha-tech/Agri-Echo.git

cd agri-echo/backend


### 2. Create Virtual Environment

python -m venv venv
venv\Scripts\activate


### 3. Install Dependencies

pip install flask tensorflow numpy pillow


### 4. Run Application

python app.py


### 5. Open in Browser

http://127.0.0.1:5000


---

## 📊 How It Works
1. User uploads crop image
2. Image is processed using ML model
3. Disease is predicted
4. Result + solution shown in selected language
5. Voice output reads the result
6. Data stored in database for analytics

---

## 🌍 Offline Capability
AgriEcho is designed to work in low or no internet environments. The AI model, backend, and database run locally, making it suitable for rural farming areas.

---


## 🚀 Future Improvements
- Mobile application version
- More crop disease datasets
- Real-time camera detection
- Advanced analytics dashboard

---


## 🙌 Acknowledgement
Developed as part of a hackathon project to support farmers with AI-driven solutions.





