from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import sqlite3

app = Flask(__name__)

# Load model
model = load_model("../my_model.keras")

# Classes
classes = ["Early Blight", "Late Blight", "Healthy"]

# Translations
translations = {
    "Early Blight": {"en": "Early Blight", "ta": "ஆரம்ப இலை நோய்", "hi": "प्रारंभिक झुलसा रोग"},
    "Late Blight": {"en": "Late Blight", "ta": "பின்னர் இலை நோய்", "hi": "देर से झुलसा रोग"},
    "Healthy": {"en": "Healthy", "ta": "ஆரோக்கியமானது", "hi": "स्वस्थ"}
}

# Remedies
remedies = {
    "Early Blight": {
        "en": "Use neem oil spray and remove affected leaves.",
        "ta": "வேப்பெண்ணெய் தெளிக்கவும் மற்றும் பாதிக்கப்பட்ட இலைகளை அகற்றவும்.",
        "hi": "नीम तेल का छिड़काव करें और प्रभावित पत्तियों को हटा दें।"
    },
    "Late Blight": {
        "en": "Apply fungicide and avoid overwatering.",
        "ta": "பூஞ்சை மருந்து பயன்படுத்தவும் மற்றும் அதிக நீர் விட வேண்டாம்.",
        "hi": "फफूंदनाशक का उपयोग करें और अधिक पानी देने से बचें।"
    },
    "Healthy": {
        "en": "Your plant is healthy. No action needed.",
        "ta": "உங்கள் செடி ஆரோக்கியமாக உள்ளது. எதுவும் செய்ய தேவையில்லை.",
        "hi": "आपका पौधा स्वस्थ है। कोई कार्रवाई आवश्यक नहीं है।"
    }
}

# ---------------- UI ROUTES ----------------

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/signup_page')
def signup_page():
    return render_template("signup.html")

@app.route('/profile')
def profile():
    return render_template("profile.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


# ---------------- AUTH ----------------

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data['username']
    password = data['password']

    conn = sqlite3.connect("agri.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

    return jsonify({"message": "User registered successfully"})


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    conn = sqlite3.connect("agri.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid credentials"})


# ---------------- PREDICT ----------------

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    path = "temp.jpg"
    file.save(path)

    img = image.load_img(path, target_size=(224,224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    prediction = model.predict(img_array)
    result = classes[np.argmax(prediction)]

    language = request.form.get("lang", "en")

    disease_text = translations[result][language]
    solution_text = remedies[result][language]

    username = request.form.get("username", "guest")

    # Save to DB
    conn = sqlite3.connect("agri.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO predictions (username, disease, solution) VALUES (?, ?, ?)",
        (username, disease_text, solution_text)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "disease": disease_text,
        "solution": solution_text
    })


# ---------------- HISTORY ----------------

@app.route('/history')
def history():
    username = request.args.get("username")

    conn = sqlite3.connect("agri.db")
    cursor = conn.cursor()

    cursor.execute("SELECT disease FROM predictions WHERE username=?", (username,))
    data = cursor.fetchall()

    conn.close()

    result = [{"disease": d[0]} for d in data]

    return jsonify(result)


# ---------------- ANALYTICS ----------------

@app.route('/analytics')
def analytics():
    username = request.args.get("username")

    conn = sqlite3.connect("agri.db")
    cursor = conn.cursor()

    cursor.execute("SELECT disease FROM predictions WHERE username=?", (username,))
    data = cursor.fetchall()

    conn.close()

    freq = {}
    for d in data:
        disease = d[0]
        freq[disease] = freq.get(disease, 0) + 1

    return jsonify(freq)


# ---------------- RUN ----------------

app.run(debug=True)