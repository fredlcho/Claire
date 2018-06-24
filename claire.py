import speech_recognition as sr
import pyttsx3
import random
import webbrowser
r = sr.Recognizer()
mic = sr.Microphone()


#webbrowser.register('google-chrome',Chrome('google-chrome'))
print(webbrowser._browsers)

positiveresponses = ["that's great!","cool!","terrific!","awesome!"]
negativeresponses = ["oh no what happened?", "that's awful", "feel better soon", "that's terrible"]
userpositiveresponses = ["good","I'm good thanks","I'm great","amazing","I'm terrific"]
usernegativeresponses = ["not so good","terrible","could be better","I'm awful"]

chromepath = "C:\\Users\\Owner\\AppData\\Local\\Google\\Chrome\\Application"

def conversation(audio,engine):
   engine.say("Hello, how are you Fred?")
   engine.runAndWait()
   audio = r.listen(source)
   if r.recognize_google(audio) in userpositiveresponses:
      x = random.choice(positiveresponses)
      engine.say(x)
      engine.runAndWait()
   elif r.recognize_google(audio) in usernegativeresponses:
      x = random.choice(negativeresponses)
      engine.say(x)
      engine.runAndWait()


#greetings = ['hi Claire','hey Claire',
engine = pyttsx3.init()
with mic as source:
    while True:
       try:
          audio = r.listen(source)
          print(r.recognize_google(audio))
          if r.recognize_google(audio) == "hi Claire":
             conversation(audio,engine)
          elif r.recognize_google(audio) == "Claire open ninjas stream":
             engine.say("now opening ninja's stream")
             webbrowser.get('chrome %s').open_new_tab('http://www.twitch.tv/ninja')
             engine.runAndWait()
             print("haha")
       except sr.UnknownValueError:
          engine.say("I didn't quite catch that")
          engine.runAndWait()
       
       
