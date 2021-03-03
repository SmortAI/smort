import speech_recognition as sr
import platform
import os


Microphone = sr.Microphone()


recognizer = sr.Recognizer()

with Microphone as source:
    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_sphinx(audio)
        print("text:{}".format(text))
    except:
        print("fuck")
