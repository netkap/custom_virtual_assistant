import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Bro, your virtual assistant. How may I assist you?")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Unable to Recognize your voice. Please try again...")
        return "None"
    return query

def sendEmail(to, subject, body):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', 'yourpassword')
        message = f'Subject: {subject}\n\n{body}'
        server.sendmail('youremail@gmail.com', to, message)
        server.close()
        speak("Email sent successfully!")
    except Exception as e:
        print(e)
        speak("Sorry, I am not able to send this email at the moment. Please try again later.")

def setReminder():
    speak("What should I remind you about?")
    reminder = takeCommand()
    speak("In how many minutes?")
    minutes = int(takeCommand())
    seconds = minutes * 60
    time.sleep(seconds)
    speak(f"Reminder: {reminder}")
def takeNotes():
    speak("What should I write down?")
    notes = takeCommand()
    with open("notes.txt", "a") as f:
        f.write(notes + "\n")
    speak("Note added successfully.")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            webbrowser.open("https://open.spotify.com/")
            speak("Playing music on Spotify")
            time.sleep(10)
            # press space key to start playing music
            keyboard.press_and_release('space')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'send email' in query:
            try:
                speak("What should I say?")
                body = takeCommand()
                speak("To whom should I send this email?")
                to = input()
                speak("What should be the subject of the email?")
                subject = takeCommand()
                sendEmail(to, subject, body)
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email at the moment. Please try again later.")

        elif 'goodbye' in query:
            speak("Goodbye!")
            break
