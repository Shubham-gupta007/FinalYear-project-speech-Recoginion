import pyttsx3

engine = pyttsx3.init()

sound = engine.getProperty('voices')
rate = engine.getProperty('rate')


engine.setProperty('rate', rate-65)


#for voice in voices:
engine.setProperty('voice', sound[1].id)

engine.say('Firstly i introduce my mentor.') 
engine.say('my mentor name is Shubham Gupta ')

engine.say('And he was presently working on python speech libraries ')


engine.runAndWait()