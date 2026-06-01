# BABY_SIRI_VOICEASSISTANT_GENAI
# 🎙️ Baby Siri Voice Assistant

A simple AI-powered Voice Assistant built using **Python**, **Streamlit**, **Speech Recognition**, **Text-to-Speech (TTS)**, and **Groq LLM**.

The assistant can:

* 🎤 Listen to your voice
* 📝 Convert speech to text
* 🤖 Generate intelligent responses using Groq's Llama Model
* 🔊 Speak responses back using Text-to-Speech
* 💬 Maintain conversation history
* 🎛️ Allow voice customization (Boy/Girl Voice)

---

## 🚀 Features

* Real-time Speech-to-Text
* AI Chat Responses using Groq API
* Text-to-Speech Output
* Conversation History
* User-Friendly Streamlit Interface
* Voice Gender Selection
* Clear Chat Functionality

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Groq API
* SpeechRecognition
* Pyttsx3
* Python Dotenv

---

## 📂 Project Structure

```bash
Baby-Siri-Voice-Assistant/
│
├── app.py
├── .env
├── requirements.txt
├── README.md
└── assets/
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/Baby-Siri-Voice-Assistant.git

cd Baby-Siri-Voice-Assistant
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from:

https://console.groq.com

---

## ▶️ Run Application

```bash
streamlit run app.py
```

The application will start at:

```bash
http://localhost:8501
```

---

## 📦 Required Packages

Create a `requirements.txt` file:

```txt
streamlit
groq
python-dotenv
SpeechRecognition
pyttsx3
pyaudio
```

---

## 🎯 How It Works

1. User clicks **Start Voice Input**
2. Assistant listens through microphone
3. Speech is converted to text
4. User query is sent to Groq LLM
5. AI generates a response
6. Response is displayed on screen
7. Text-to-Speech reads the response aloud

---

## 🖥️ User Interface

### Sidebar Controls

* Enable/Disable Text-to-Speech
* Select Voice Gender
* Start Voice Input
* Clear Chat

### Main Window

* Displays conversation history
* Shows user and assistant messages

---

## 🔒 Environment Variables

| Variable     | Description       |
| ------------ | ----------------- |
| GROQ_API_KEY | Your Groq API Key |

---

## 🌟 Future Improvements

* Wake Word Detection ("Hey Siri")
* Multiple Language Support
* Voice Cloning
* Chat Export Feature
* Mobile Friendly Interface
* Continuous Conversation Mode

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Vamsipriya**

AI & Machine Learning Enthusiast | Python Developer | Generative AI Learner

If you like this project, don't forget to ⭐ the repository!
