import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("Good evening")

def recieveCommands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING......")
        r.pause_threshold=1
        audio = r.listen(source)

        try:
            print("PROCESSING...")
            query = r.recognize_google(audio,language="en-in")
            print(f"You said : {query}\n")
        except Exception as e:
            print("I didn't catch that. Please repeat :)")
            return "None"
        return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jayeshxxxx@gmail.com','xx')
    server.sendmail('xx@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    greetings()
    while 1:
        query = recieveCommands().lower()

        if 'wikipedia' in query:
            speak("searching on wikipedia...")
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=5)
            speak("According to wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open leetcode' in query:
            webbrowser.open("leetcode.com")
        elif 'open soundcloud' in query:
            webbrowser.open("soundcloud.com")
        elif 'the time' in query:
            curtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {curtime}")
        elif 'email to jayesh' in query:
            try:
                speak("What should i say?")
                content = recieveCommands()
                to="jayeshxxxzzz@gmail.com"
                sendEmail(to,content)
                speak ("E-Mail sent successfully")
            except Exception as e:
                print(e)
                speak("Sorry sir. I couldn't send the E-Mail at the moment")

