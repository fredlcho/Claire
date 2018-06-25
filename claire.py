import speech_recognition as sr
import pyttsx3
import random
import webbrowser
import re
r = sr.Recognizer()
r.energy_threshold = 5000
mic = sr.Microphone()


#webbrowser.register('google-chrome',Chrome('google-chrome'))
print(webbrowser._browsers)
#chrome = webbrowser.get('chrome %s')
positiveresponses = ["that's great!","cool!","that's terrific!","awesome!"]
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
   r.energy_threshold = 10000
   while True:
      r.energy_threshold = 10000
      try:
         r.energy_threshold = 10000
         print(r.energy_threshold,"1")
         audio = r.listen(source)
         r.adjust_for_ambient_noise(source, duration = 1)
         
         if r.recognize_google(audio) == "hi Claire":
            conversation(audio,engine)
         elif r.recognize_google(audio) == "Claire open ninjas stream":
            engine.say("now opening ninja's stream")
            webbrowser.get('chrome %s').open_new_tab('http://www.twitch.tv/ninja')
            engine.runAndWait()
            #print("haha")
         elif r.recognize_google(audio) == "Claire open toast stream":
            engine.say("now opening toast's stream")
            webbrowser.get('chrome %s').open_new_tab("https://www.twitch.tv/disguisedtoasths")
            engine.runAndWait()
         elif r.recognize_google(audio) == "thank you":
            engine.say("you're welcome")
            engine.runAndWait()
         elif r.recognize_google(audio) == "Claire play some groovy music":
            engine.say("playing some groovy music")
            webbrowser.get('chrome %s').open_new_tab("https://www.youtube.com/watch?v=Lrle0x_DHBM&list=RDQMeof1lCt9BNY&start_radio=1")
            r.energy_threshold = 10000
            print(r.energy_threshold,"2")
            engine.runAndWait()
         else:
            print("not an error, but not valid command")
      except sr.UnknownValueError:
         engine.say("I didn't quite catch that")
         engine.runAndWait()
       
       
