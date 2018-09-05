#Only for volume

import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')


engine.setProperty('rate', rate-50)


volume = engine.getProperty('volume')
engine.setProperty('volume', volume+0.75)

sound = engine.getProperty('voices')

engine.setProperty('voice', sound[1].id)


engine.say('Now let start the presentation')

engine.runAndWait()