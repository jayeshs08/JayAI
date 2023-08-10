import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import openai
import webbrowser
import os
import smtplib
from googlesearch import search
from AppOpener import open
from config import apikey

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def openaiuse(prompt):
    openai.api_key = apikey
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Write a generic cover letter for me as a software engineer fresher."
            },
            {
                "role": "user",
                "content": ""
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    speak(response["choices"][0]["text"])
    print(response["choices"][0]["text"])

def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir, Jay A.I is active")
    elif hour>=12 and hour<18:
        speak("good afternoon sir, Jay A.I is active")
    else:
        speak("Good evening sir, Jay A.I is active")

def recieveCommands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING......")
        r.pause_threshold=0.5
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
        sites = [["youtube","https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],["google","https://www.google.co.in"],
                 ["leetcode","https://www.leetcode.com"], ["github","https://www.github.com"], ["linkedin","https://www.linkedin.com"]]

        if "open" in query:
            for site in sites:
                if f"Open {site[0]}".lower() in query:
                    speak(f"Opening {site[0]} right now sir.")
                    webbrowser.open(site[1])

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

        elif 'search' in query:
            speak("These are the search results from Google.")
            search(query, num_results=5)
        elif 'the time' in query:
            curtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {curtime}")
        elif 'start telegram' in query:
            speak("Opening telegram sir.")
            open("telegram", throw_error=True)

        if "tell me" in query:
            openaiuse(prompt=query)



