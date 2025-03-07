
import speech_recognition as sr
import pyttsx3

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ascolto...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="it-IT")
            print(f"Hai detto: {text}")
            return text
        except sr.UnknownValueError:
            print("Non ho capito")
            return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
