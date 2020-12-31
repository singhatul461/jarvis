from sys import path
from urllib.parse import uses_query
import pyttsx3 # pip install pyttsx3
import datetime  #for time 
import speech_recognition as sr # pip install speechRecognition 
import wikipedia
import webbrowser 
import os              #opreating system 
engine = pyttsx3.init()  #it is used for audio


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("wellcome boss!")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("good morning boss!")
    elif hour  >=12 and hour<18:
        speak("good afternoon boss")
    elif hour  >=18 and hour<24:
        speak("good Evening boss")
    else:
        speak("good night boss")
    speak("jarvis at your service, please tell me how can i help you boss ?")
    
def takecomand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recongnizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        speak("say that again please....")
        return "noone"
    return query

if __name__== "__main__":
    wishme()
    while True:
        query = takecomand().lower()

        # logic for executing task based on query 
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'open the youtube' in query:
            webbrowser.open('youtube.com')
            speak("opening youtube, anything else boss")
        elif 'open the google' in query:
            webbrowser.open('google.com')
            speak("opening google")
        elif 'open the stack overflow' in query:
            webbrowser.open('stackoverflow.com')
            speak("open starck overflow, anything else boss")

        elif 'play the music' in query:
            music_dir = 'D:\\Non critical\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[5]))
            speak("as you wish boss, anything else boss")
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%H:%S")
            speak(f"boss, the time is {strtime}")
        elif 'how are you' in query:
            speak("awesome boss!")
        elif 'what is jigar doing' in query:
            speak("jigar is using phone")
        elif 'what is neha' in query:
            speak("neha is nonsence")
        elif 'what can you do for me' in query:
            speak("i can massege your love ones")
        elif 'ok jarvis' in query:
            speak("yes boss")
        elif 'no thanks' in query:
            speak("ok boss, thank you for using me!")
        elif 'can you complete my exam' in query:
            speak("cheating is not good for future, boss")
        elif 'who is my class teacher' in query:
            speak("jigisha mam is your class teacher, she teach you computer programming and html also")
        elif 'who is my special one' in query:
            speak("can i tell you in, private?")
        elif 'tell me something about my life' in query:
            speak("you cheated by someone")
        elif 'open code' in query:
            codepath = "C:\\Users\\singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            speak("opening code editor")
        elif 'open data drive' in query:
            path = "D:\\"
            os.startfile(path)
            speak("opening data drive")
        elif 'play ironman music' in query:
            music_dir = 'D:\\Non critical\\iron man'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[1]))
            speak("as you wish boss")
        elif 'tell me something better' in query:
            speak('the wheather is too good, you should hang out in out door')
        elif 'jarvis' in query:
            speak("yo boss")
        elif 'where is Riddhi?' in query:
            speak("she is in baroda")
        elif 'where is my father' in query:
            speak("your father had hloiday today, and he is using phone.")
        elif 'how is the wheather outside' in query:
            speak("wheather is too good, in my calculation, the room temprature is 30 degree celcius")
        elif 'happy new year' in query:
            speak("happy new year boss, have a great year ever of this era")