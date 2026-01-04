import pyttsx3
import speech_recognition as sr
import datetime 
import wikipedia
import time
import webbrowser
import os
import smtplib

engine  = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)
 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        greeting = "Good Morning"
    elif hour >= 12 and hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    speak(greeting + ". I am your virtual assistant Zira. How may I help you?")
    

def  takeCommand():
    #takes microphone input from user and returns string output
    r= sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query
    
    except Exception as e:
        #print(e)
        print("Error Occrued. Say that again please...")
        return ""
    
def sendEmail(to, content):
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('myemail@gmail.com', 'password')
    server.sendmail('myemail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            print("Searching wikipedia...")
            time.sleep(0.5)

            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)

            speak(results)
            print(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif "play music" in query:
            music_dir = 'D:\\bACKUP SAMSUNG\\Videos and Audios'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            print(f"The time is {strTime}")

        elif 'open vs code' in query:
            codePath= "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "email to harry" in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "myemail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            
            except Exception as e:
                print(e)
                speak("Unable to send email at the moment")
        
        elif "quit" in query:
            speak("Okay... I am going to sleep now")
            time.sleep(1)
            exit()




        
            

