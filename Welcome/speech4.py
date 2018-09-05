import pyttsx3
engine = pyttsx3.init()

rate = engine.getProperty('rate')

engine.setProperty('rate', rate-50)

sound = engine.getProperty('voices')

engine.setProperty('voice', sound[1].id)



engine.say('And Now i will introduce myself')

engine.say('My name is SIRI DEVI and i am personal assistant of Shubham')


engine.runAndWait()