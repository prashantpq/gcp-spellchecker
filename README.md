# ✨ Contextual Spell Checker

[![Deployed on Render](https://img.shields.io/badge/Deployed-Render-blue)](https://spell-checker-2-ho7v.onrender.com)

This project is a **contextual English grammar and spell checker** built using:

- 🐍 **Flask** for backend API  
- ⚡ **Groq LLM API** for contextual correction  
- 🌐 **Beautiful responsive frontend** for user interaction  
- 🚀 **Deployed on Render**

---

## 🔗 **Live Demo**

👉 [View it here](https://spell-checker-2-ho7v.onrender.com)

---

## ✨ **Features**

✅ Highlights corrected words  
✅ Uses advanced LLM for grammar context understanding  
✅ Responsive UI for desktop and mobile  
✅ Copies corrected text with one click  
✅ Clean and minimal design

---

## 💻 **Setup Locally**

1. **Clone the repository**

```bash
git clone https://github.com/prashantpq/spell-checker.git
cd spell-checker

### 2️⃣ Create & Activate a Virtual Environment:
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Required Dependencies:
```sh
pip install -r requirements.txt
```

---

## 🛠 Running the Project Locally

1️⃣ Start the Flask application:
```sh
python main.py
```
2️⃣ Open your browser and go to:
   **http://127.0.0.1:8000/**
3️⃣ Enter a sentence with spelling mistakes and check the corrected text.

---

---

## 📂 Project Structure
```
spell-checker/
├── templates/
│   ├── index.html  # Frontend UI (HTML, CSS, JS)
├── main.py         # Flask API handling spell checking
├── requirements.txt  # Project dependencies
├── app.yaml        # Google Cloud App Engine configuration
├── README.md       # Project documentation
└── config.py       # (Optional) Configuration settings
```

---
