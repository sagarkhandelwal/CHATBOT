import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser 
import os
import smtplib
import random
import sys
import bs4
import urllib
import urllib.parse
import urllib.request
import re

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    print('BOSS: '+ audio)
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

wishMe()
speak("I AM BOSS SIR. PLEASE TELL ME HOW MAY I HELP YOU")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #r.adjust_for_ambient_noise(source)
        r.energy_threshold=1000
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print("User : "+query+'\n')

    except Exception as e:
            
        print("Say that again please...")
        print('TYPE THE COMMAND ')
        query=str(input('COMMAND: '))
    return query

'''def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sagarkhandelwal187@gmail.com', 'your-password')
    server.sendmail('sagarkhandelwal187@gmail.com', to, content)
    server.close()'''

if __name__ == "__main__":
    
    
    
    while True:
  
        query = takeCommand().lower()

      
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            
           
                query_string = urllib.parse.urlencode({'search_query':input('ENTER THE VIDEO YOU WANT TO SEARCH\n')})
                html_content=urllib.request.urlopen("https://www.youtube.com/results?"+query_string)
                search_results=re.findall(r'href=\"\/watch\?v=(.{11})',html_content.read().decode())
                x="https://www.youtube.com/watch?v="+search_results[0]
                webbrowser.open(x)


        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com")
            
        elif 'open geeks for geeks' in query:
            webbrowser.open("www.geeksforgeeks.com")

        elif 'play music' in query:
            music_dir = 'H:\\16GB CARD\\00New folder (2)'
            songs = os.listdir(music_dir)
            
            a=random.choice(songs)
            os.startfile(os.path.join(music_dir,a))
            speak('HERE IS YOUR MUSIC!ENJOY....')
        elif 'open gmail' in query:
            webbrowser.open("www.gmail.com")
        
        elif 'open maps' in query:
            webbrowser.open('https://www.google.com/maps/@26.2037599,78.1530435,14z')

        elif 'the time' in query or 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'bye' in query or 'exit' in query or 'stop' in query:
            speak('BYE SIR HAVE A NICE DAY....')
            sys.exit()
        else:
            query=query
            speak('SEARCHING.....')
            try:
                results=wikipedia.summary(query,sentences=2)
                speak('GOT IT..')
                speak('WIKIPEDIA SAYS -')
                
                speak(results)
            except:
                webbrowser.open('www.google.com')
        speak('NEXT COMMAND....')       
