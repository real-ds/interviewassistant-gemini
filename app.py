# app.py
import streamlit as st
import tempfile
import speech_recognition as sr
from google import genai

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Interview Assistant", layout="centered")

# -------------------- SIDEBAR --------------------
st.sidebar.title("🔐 Configuration")
api_key = st.sidebar.text_input(
    "Enter Gemini API Key",
    type="password",
    help="Get your API key from Google AI Studio"
)

if not api_key:
    st.warning("Please enter your Gemini API key in the sidebar.")
    st.stop()

client = genai.Client(api_key=api_key)

# -------------------- UI --------------------
st.markdown("## Real-Time Interview Assistant")

st.markdown(
    """
    **An AI-powered assistant that listens to interviewer questions in real time  
    and instantly generates clear, structured, interview-ready answers.**

    Designed for:
    - Technical interviews  
    - HR & behavioral rounds  
    - Concept explanations under pressure  

    ⚡ *Listen → Understand → Respond smarter*
    """
)

audio = st.audio_input("Record interviewer question")

# -------------------- FUNCTIONS --------------------
def speech_to_text(audio_bytes):
    r = sr.Recognizer()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio_bytes)
        temp_audio_path = f.name

    with sr.AudioFile(temp_audio_path) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)

    return text

def generate_answer(question):
    prompt = f"""
You are an interview assistant.
Give a concise, professional, interview-ready answer.

Question:
{question}
"""
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    if hasattr(response, "text") and response.text:
        return response.text

    return response.candidates[0].content.parts[0].text

# -------------------- LOGIC --------------------
if audio:
    try:
        with st.spinner("Listening and transcribing..."):
            question_text = speech_to_text(audio.getvalue())

        st.subheader("🗣️ Detected Question")
        st.write(question_text)

        with st.spinner("Generating answer..."):
            answer = generate_answer(question_text)

        st.subheader("✍️ Suggested Answer")
        st.write(answer)

    except Exception as e:
        st.error("An error occurred")
        st.exception(e)
