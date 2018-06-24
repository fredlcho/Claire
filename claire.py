import speech_recognition as sr
import pyttsx3
r = sr.Recognizer()
mic = sr.Microphone()

engine = pyttsx3.init()
while True:
    with mic as source:
        audio = r.listen(source)

#print(r.recognize_google(audio))
    if r.recognize_google(audio) == "hi Claire":
        engine.say("Hello, how are you?")
        engine.runAndWait()
