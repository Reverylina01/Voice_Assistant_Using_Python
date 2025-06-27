import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import openai

# API Key (Replace with your actual key)
OPENAI_API_KEY = "Your_Key"
# Initialize OpenAI
openai.api_key = OPENAI_API_KEY

# Initialize speech recognition and text-to-speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()
reminders = []

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower().strip()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Speech service is down.")
        return ""

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful voice assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = response['choices'][0]['message']['content']
        speak(reply)
    except Exception as e:
        speak("There was an error connecting to OpenAI.")
        print("OpenAI Error:", e)

def open_app(app_name):
    app_paths = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "chrome": r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    }
    path = app_paths.get(app_name.lower())
    if path:
        os.startfile(path)
        speak(f"Opening {app_name}")
    else:
        speak("I don't know that app.")

def add_reminder(task):
    reminders.append(task)
    speak(f"Reminder added: {task}")

def list_reminders():
    if reminders:
        speak("Here are your reminders:")
        for task in reminders:
            speak(task)
    else:
        speak("You have no reminders.")

def handle_command(command):
    if 'time' in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    elif 'youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif 'google' in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif 'chat' in command or 'talk' in command:
        speak("What would you like to talk about?")
        question = listen()
        if question:
            chat_with_gpt(question)

    elif 'open' in command and 'app' in command:
        speak("Which app?")
        app = listen()
        if app:
            open_app(app)

    elif 'remind' in command:
        speak("What should I remind you about?")
        task = listen()
        if task:
            add_reminder(task)

    elif 'show reminders' in command or 'list reminders' in command:
        list_reminders()

    elif 'your name' in command:
        speak("I am your Python voice assistant.")

    elif 'stop' in command or 'exit' in command or 'quit' in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I didn't understand that.")

def main():
    speak("Hello! I am your voice assistant. How can I help you today?")
    while True:
        command = listen()
        if command:
            handle_command(command)

if __name__ == "__main__":
    main()
