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
    tts = gTTS(str(audioString), lang='hi')
    tts.save("audio_hindi.mp3")
    mixer.music.load('audio_hindi.mp3')
    mixer.music.play()
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("कुछ कहें : Say something!")
        audio = r.listen(source,phrase_time_limit=5)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("अपने कहा: " + data + "'")
        tts=gTTS(str(data), lang='hi')
        tts.save("audio_hindi2.mp3")
        mixer.music.load('audio_hindi2.mp3')
        mixer.music.play()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
def jarvis(data):
    if "kya haal hai" in data:
        speak("मैं ठीक हूँ")
	
    if "kya kar sakate ho" in data:
        speak("जो भी आप सर चाहते हैं")
		
    if "aaj ki date" in data:
        speak(strftime("%a, %d %b %Y %H:%M:%S +0000"))
 
    if "abhi ka samay" in data:
        speak(ctime())
	
    if "London ka samay" in data:
        speak(datetime.datetime.now().astimezone(timezone('Europe/London')))
	
    if "Madrid ka samay" in data:
        speak(datetime.datetime.now().astimezone(timezone('Europe/Madrid')))
		
    if "Paris ka samay" in data:
        speak(datetime.datetime.now().astimezone(timezone('Europe/Paris')))
		
    if "Moscow ka samay" in data:
        speak(datetime.datetime.now().astimezone(timezone('Europe/Moscow')))		
#    if "add item" in data:
#    if "open control panel" in data:
#    if "open download folder" in data:

#    if  "open documents" in data:
        #os.system("download")
    if "open disk d" in data:
        names = os.popen('dir D:\\').readlines()
        for name in names:
            speak(name)

#    if "cya siri" in data: stop listening 


    if "I am hungry" in data:
        speak("how much money you have")
    if "25 rupees only" in data:
        speak("go to restaurant or  buy a hamburger")
    if "no money" in data:
        speak("go to sleep")	
"""    
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Shubham, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
 """
# initialization
time.sleep(2)
speak("नमस्ते शुभम, मैं आपके लिए क्या कर सकती हूं?")
while 3:
    data = recordAudio()
    jarvis(data)
	


"""
am i hungry?
yes or no
if yes: have i 25rs only 
if no: go to sleep

if yes : go to restauran
if no: buy a hamburger

"""	

