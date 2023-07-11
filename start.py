import speech_recognition
import pyttsx3
import os
from gtts import gTTS
from sound import Sound

en = 'en'

recognizer = speech_recognition.Recognizer()
engine = pyttsx3.init()
while True:
    try:

        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()
            
            if text == "mute":
                volume.SetMute(0, None)
                # engine.say("nothing")
                # engine.runAndWait()

            print(f"Regognized {text}")
    except speech_recognition.UnknownValueError():
        recognizer - speech_recognition.Recognizer()
        continue 