# 🎯 Real-Time Interview Assistant

An AI-powered web application that listens to interviewer questions in real time and instantly generates clear, professional, interview-ready answers using **Google Gemini**.

This project is designed as a **quick prototype** for interview assistance, demos, and portfolio use.

---

## 🚀 Features

- 🎙️ Record interviewer questions using microphone  
- 🗣️ Automatic speech-to-text conversion  
- 🧠 AI-generated concise and structured answers  
- 🔐 Secure Gemini API key input via UI (no `.env` required)  
- ⚡ Fast responses with Gemini LLM  
- 🌐 Simple and clean Streamlit interface  

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|------------|
| Frontend | Streamlit |
| AI Model | Google Gemini (`google-genai`) |
| Speech-to-Text | SpeechRecognition |
| Language | Python |

---

## 📂 Project Structure

```
interviewassistant-gemini/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Local Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/real-ds/interviewassistant-gemini
cd interviewassistant-gemini
```

---

### 2️⃣ Create Virtual Environment (Recommended)
```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**macOS / Linux**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application
```bash
streamlit run app.py
```

The app will open in your browser at:
```
http://localhost:8501
```

---

## 🔑 Getting a Gemini API Key

1. Go to **Google AI Studio**  
2. Create a new API key  
3. Copy the key  
4. Paste it into the **sidebar input field** in the application  

🔒 The key is masked and not stored.

---

## 🧪 How to Use

1. Enter your **Gemini API key** in the sidebar  
2. Click **Record interviewer question**  
3. Speak the interviewer’s question clearly  
4. View:
   - 🗣️ Detected question  
   - ✍️ AI-generated interview-ready answer  

---

## ☁️ Deployment (Streamlit Cloud)

1. Push this project to GitHub  
2. Go to **https://streamlit.io → Deploy**  
3. Select your repository and `app.py`  
4. Deploy 🚀  

> 💡 For production deployments, Streamlit Secrets are recommended for API keys.

---

## ⚠️ Limitations

- Requires internet connection  
- Audio quality affects transcription accuracy  
- Prototype-level error handling  
- Not intended for misuse or policy violations  

---

## 🛣️ Future Enhancements

- Resume-aware answer generation  
- Interview mode selection (HR / Technical / Behavioral)  
- Streaming answers (token-by-token)  
- Always-listening stealth mode  
- Mobile-optimized UI  

---

## 📜 Disclaimer

This project is intended for **educational, research, and prototyping purposes only**.  
Users are responsible for complying with interview policies and ethical guidelines.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to fork and improve it!
