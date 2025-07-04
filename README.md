# 🧠 Python Voice Assistant with ChatGPT 🎙️💬

A voice-activated personal assistant built using Python, `speech_recognition`, and OpenAI's ChatGPT API. This assistant can understand your spoken commands and respond intelligently, open websites or apps, give the time, and even remind you of tasks.

---

## 🎯 Key Features

| Feature                | Description                                                      |
|------------------------|------------------------------------------------------------------|
| 🔊 Voice Recognition   | Uses your microphone to listen for commands                      |
| 🗣 Text-to-Speech       | Speaks responses back to you using `pyttsx3`                    |
| 🧠 ChatGPT Integration | Have conversations powered by GPT-3.5 or GPT-4                   |
| 🕒 Time Reporting      | Tells the current time                                            |
| 🌐 Web Access          | Opens YouTube, Google, and other URLs in your browser            |
| 🧮 App Launcher        | Opens apps like Notepad, Calculator, and Chrome (customizable)   |
| 📝 Reminders           | Add and list simple voice reminders                              |
| 🔐 Secure API Option   | Use `.env` file for hiding sensitive keys (recommended)           |

---

## 📁 Project Structure

voice-assistant/
│
├── assistant.py # Main voice assistant script
├── requirements.txt # Dependencies list
├── .gitignore # Files/folders to ignore (e.g., pycache)
├── .env (optional) # Store your OpenAI API key securely (not committed)
└── README.md # This file

---

## 🔧 Prerequisites

You’ll need:

- Python 3.7+
- Working microphone
- OpenAI API key
- Internet connection (for ChatGPT)

---

## 🛠️ Installation & Setup

### 1. Clone this repo:

```bash
git clone https://github.com/yourusername/voice-assistant.git
cd voice-assistant
Install the required libraries:
bash
Copy
Edit
pip install -r requirements.txt
If pyaudio fails on Windows, download a .whl from
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio and install manually:

bash
Copy
Edit
pip install path/to/downloaded/pyaudio‑*.whl
🔐 Add Your OpenAI API Key
Option 1: (Simple, insecure)
Edit assistant.py and replace:

python
Copy
Edit
openai.api_key = "sk-Your-Key-Here"
Option 2: (Secure, recommended)
Create a .env file in your project folder:

env
Copy
Edit
OPENAI_API_KEY=sk-your-key-here
Install dotenv:

bash
Copy
Edit
pip install python-dotenv
Modify assistant.py:

python
Copy
Edit
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
🚀 How to Run
In the terminal:

bash
Copy
Edit
python assistant.py
Say your command after hearing the assistant's greeting.

🧠 Example Voice Commands
You Say	Assistant Does
"What time is it?"	Tells the current time
"Open YouTube"	Opens https://youtube.com
"Open Google"	Opens https://google.com
"Remind me to drink water"	Adds to internal reminder list
"Show reminders"	Reads out all saved reminders
"Open app" → "Notepad"	Opens Notepad
"Chat with me" → "How's the weather?"	Sends to ChatGPT & speaks response
"What is your name?"	Tells its name
"Exit" or "Stop"	Exits the assistant

🧪 How It Works (Tech Stack)
🎙 speech_recognition to capture voice input

🔉 pyttsx3 for offline speech output

🌐 webbrowser and os to launch apps and URLs

🧠 openai.ChatCompletion for AI conversations

📅 datetime to report current time

📸 Screenshots / Demo
(Add terminal screenshots or animated GIFs here)

📦 Future Improvements
Add wake-word like “Hey Assistant”

GUI version using Tkinter or PyQt

Persistent reminder storage in .txt or .json

Add more apps and websites

Better NLP with spaCy or transformers

🛠 Troubleshooting
Q: It doesn’t hear me
✅ Check your microphone input device in system settings
✅ Try increasing recognizer.adjust_for_ambient_noise(source, duration=1)

Q: pyaudio install fails
✅ Use precompiled .whl file for Windows (see above)

Q: OpenAI error
✅ Make sure your API key is valid and internet is working

🔗 Credits
🧠 OpenAI API — https://platform.openai.com/

🔉 pyttsx3 — Offline TTS engine

🎙️ SpeechRecognition — Google Speech API interface

🧑 Built by Your Name

📄 License
MIT License — free to use, modify, and distribute. Credit appreciated!

💬 Have fun talking to your assistant!
Feel free to ⭐ star the repo if you like it!
