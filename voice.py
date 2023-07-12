import speech_recognition
import pyttsx3
import os
from gtts import gTTS
import webbrowser
en = 'en'

recognizer = speech_recognition.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('rate', 125)
while True:
    try:

        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()
            
            if text == 'change language to polish':
                en = 'pl'
                engine.say("Język zmieniony")
                engine.runAndWait()
                


            if text == "open web":
                engine.say("Opening")
                engine.runAndWait()
                webbrowser.open("https://recrash.vercel.app/map",  new=2)
                

            print(f"Regognized {text}")
    except speech_recognition.UnknownValueError():
        recognizer - speech_recognition.Recognizer()
        continue 