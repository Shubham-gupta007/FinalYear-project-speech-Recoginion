import pyttsx3

engine = pyttsx3.init()

sound = engine.getProperty('voices')

rate = engine.getProperty('rate')


engine.setProperty('rate', rate-65)

#for voice in voices:
engine.setProperty('voice', sound[1].id)

engine.say('And my comentor name is Tabish Khan')

engine.say('And they are copartner of Shubham Gupta ')

engine.runAndWait()