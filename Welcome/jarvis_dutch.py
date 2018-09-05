#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
from time import ctime
from time import strftime, gmtime
import time
import datetime
from pytz import timezone
from os import popen
import os
from gtts import gTTS
 
from pygame import mixer
mixer.init()

 
def speak(audioString):
    print(audioString)
    tts = gTTS(str(audioString), lang='nl')
    tts.save("audio_dutch1.mp3")
    mixer.music.load('audio_dutch1.mp3')
    mixer.music.play()
 
def recordAudio():
    # Record Audio

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Zeg iets!:Say something!")
        audio = r.listen(source,phrase_time_limit=5)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # recognize speech using Sphinx/Google    
        #data = r.recognize_sphinx(audio)
        data = r.recognize_google(audio)
        print("Jij zei:You said" + data + "'")
        tts=gTTS(str(data), lang='nl')
        tts.save("audio_dutch2.mp3")
        mixer.music.load('audio_dutch2.mp3')
        mixer.music.play()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
def jarvis(data):
    if "hoe gaat het met je" in data:
        speak("het gaat prima met mij")
			
    if "Wat kun je voor mij doen" in data:
        speak("wat je maar wilt schat")
		
    if "vandaag dag en datum" in data:
        speak(strftime("%a, %d %b %Y %H:%M:%S +0000"))
 
    if "hoe laat is het" in data:
        speak(ctime())
	
    if "hoe laat in Londen" in data:
        speak(datetime.datetime.now().astimezone(timezone('Europe/London')))
	
    if "hoe laat in Madrid" in data:
        speak(datetime.datetime.now().astimezone(timezone('Europe/Madrid')))
		
    if "hoe laat in Parijs" in data:
        speak(datetime.datetime.now().astimezone(timezone('Europe/Paris')))
		
    if "hoe laat in Moskou" in data:
        speak(datetime.datetime.now().astimezone(timezone('Europe/Moscow')))
		
    if "hoe laat in Canberra" in data:
        speak(datetime.datetime.now().astimezone(timezone('Australia/Canberra')))	
#    if "add item" in data:
#    if "open control panel" in data:
#    if "open download folder" in data:

#    if  "open documents" in data:
        #os.system("download")
    if "open schijf d" in data:
        names = os.popen('dir D:\\').readlines()
        for name in names:
            speak(name)

#    if "cya siri" in data: stop listening 


    if "I am hungry" in data:
        speak("hoeveel geld heb je")
    if "25 rupees only" in data:
        speak("ga naar restaurant of koop een hamburger")
    if "no money" in data:
        speak("go to sleep")	

#Gk Questions
		
    if "capital of India" in data:
        speak("New Delhi")
    if "Which crop is sown on the largest area in India" in data:
        speak("rice")
    if "value of gold is determined in" in data:
        speak("London")
    if "Taj Mahal is on the banks of" in data:
        speak("Jamuna")
    if " First University in India was founded at" in data:
        speak("Calcutta")	
    if "The currency notes are printed in" in data:
        speak("Nasik")
    if "The chemical name of common salt is" in data:
        speak("Sodium Chloride")
    if "Sodium Chloride formula" in data:
        speak("NaCl")	
    if "The most populous city in the world is" in data:
        speak("Tokyo")
	
	
#Cooking

#Open System Files
    if "rekenmachine openen" in data:
        speak(os.system('start calc.exe')) 
    if "open Browser" in data:
        speak(webbrowser.get("C:\Program Files\Opera\launcher.exe %s").open("http://google.com"))
    if "Browser" in data:
        speak(webbrowser.get("C:\Program Files\Opera\launcher.exe %s").open("http://google.com"))
    if "open kladblok" in data:
        speak(os.system('start notepad.exe'))	
"""    
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Shubham, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
 """
# initialization
time.sleep(2)
speak("Hallo Shubham, wat kan ik voor je doen?")
while 3:
    data = recordAudio()
    jarvis(data)
	



