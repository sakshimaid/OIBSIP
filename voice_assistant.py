#python code for voice assistant(beginner)

import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia

# Initialize the speech recognition engine
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def take_command():
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        return query.lower()
    except Exception as e:
        return "none"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def main():
    while True:
        query = take_command()
        if query == "hello":
            speak("Hello! I'm your desktop assistant.")
        elif query == "what time is it":
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f "The time is {time}")
        elif query == "what day is it":
            day = datetime.datetime.today().strftime("%A")
            speak(f "Today is {day}")
        elif "search" in query:
            query = query.replace("search", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        elif "wikipedia" in query:
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            speak(result)
        elif query == "bye":
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()