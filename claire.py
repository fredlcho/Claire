import speech_recognition as sr
import pyttsx3
r = sr.Recognizer()
mic = sr.Microphone()


def conversation(audio,engine):
   if r.recognize_google(audio) == "hi Claire":
          print("lala")
          engine.say("Hello, how are you Frederick?")
          engine.runAndWait()
          audio = r.listen(source)
          print(r.recognize_google(audio))
          if r.recognize_google(audio) == "I'm good":
             engine.say("that's great!")
             engine.runAndWait()


#greetings = ['hi Claire','hey Claire',
engine = pyttsx3.init()
with mic as source:
    while True:
       audio = r.listen(source)
       conversation(audio,engine)


       
