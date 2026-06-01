
# Baby Siri Voice Assistant

import streamlit as st    # used to build the frontend

# Configure the frontend page
st.set_page_config(
    page_title = "Voice Assistant",
    layout = "wide"
)

# import all required libraries
import os    # used to access the API key from local env
import time
import pyttsx3
import speech_recognition as sr
from groq import Groq
from dotenv import load_dotenv

# load the API key from local environment
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Checking if API key uploaded successfully or not
if not GROQ_API_KEY:
    st.error("Missing API Key")
    st.stop()

# Intialization of LLM model
client = Groq(api_key=GROQ_API_KEY)
MODEL = "llama-3.3-70b-versatile"

# Intitalization of speech to text recognizer
@st.cache_resource
def get_recognizer():
    return sr.Recognizer()

recognizer = get_recognizer()

# inititalize the Text to Speech
def get_tts_engine():
    try:
        engine = pyttsx3.init()
        return engine
    except Exception as e:
        st.error(f"Failed to initilize the TTS Engine: {e}")
        return None

def speak(text, voice_gender = "Girl"):
    try:
        engine = get_tts_engine()
        if engine is None:
            return
        
        voices = engine.getProperty('voices')

        if voices:
            if voice_gender == 'boy':
                for voice in voices:
                    if "male" in voice.name.lower():
                        engine.setProperty("voice", voice.id)
                        break
            else:
                for voice in voices:
                    if "female" in voice.name.lower() or "zira" in voice.name.lower():
                        engine.setProperty('voice', voice.id)
                        break
        
        engine.setProperty('rate', 150)
        engine.setProperty('volumn', 0.8)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        st.error("TTS Error: {e}")



def listen_to_speech():
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration = 1)
            audio = recognizer.listen(source, phrase_time_limit=10)

            text = recognizer.recognize_google(audio)
            return text.lower()
    except sr.UnknownValueError:
        return "Sorry, I don't catch you"
    except sr.RequestError:
        return "Speech Service is not available"
    except Exception as e:
        return f"Error: {e}"

def get_ai_response(messages):
    try:
        response = client.chat.completions.create(
            model = MODEL,
            messages = messages,
            temperature=0.7
        )
        result = response.choices[0].message.content
        return result.strip() if result else "Sorry, I could not generate the response"
    except Exception as e:
        return f"Error getting the AI response: {e}"

def main():
    st.title("Baby SIRI Voice Assistant")
    st.markdown("---")

    # Intializing chat
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {"role": "system", "content": "You are a helpful voice assistant. Reply just one line"}
        ]

    # initialize the messages to print on screen
    if "messages" not in st.session_state:
        st.session_state.messages = []

    with st.sidebar:
        st.header("CONTROLS")

        tts_enabled = st.checkbox("Enter Text to Speech", value = True)

        # selecting Gender of Voice assistant
        voice_gender = st.selectbox(
            "Voice Gender",
            options = ["girl", "boy"],
            index = 0,
            help = "Choose the Gender of Voice Assistant"
        )

        if st.button("Start Voice Input", use_container_width=True, type = 'primary'):
            with st.spinner("Listening..."):
                user_input = listen_to_speech()

                if user_input and user_input not in ["Sorry, I don't catch you", "Speech Service is not available"]:
                    st.session_state.messages.append({"role": "user", "content": user_input})
                    st.session_state.chat_history.append({"role": "user", "content": user_input})

                    with st.spinner("Thinking..."):
                        ai_response = get_ai_response(st.session_state.chat_history)
                        st.session_state.messages.append({"role": "assistant", "content": ai_response})
                        st.session_state.chat_history.append({"role": "assistant", "content": ai_response})

                    if tts_enabled:
                        speak(ai_response, voice_gender)

                    st.rerun()
                
                st.markdown("---")

        if st.button("Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.session_state.chat_history = [
                        {"role": "system", "content": "You are a helpful voice assistant. Reply just one line"}
                    ]

            st.rerun()
        
    st.subheader("CONVERSTION")

    for message in st.session_state.messages:
        if message['role'] == "user":
            with st.chat_message("user"):
                st.write(message["content"])
        else:
            with st.chat_message("assistant"):
                st.write(message["content"])

    st.markdown("---")
    st.markdown(
        """
            <div style = 'text-align: center; color: #666;'>
                <p> Copyright @ Vamsipriya </p>
            </div>
        """,
        unsafe_allow_html= True
    )

if __name__ == "__main__":
    main()