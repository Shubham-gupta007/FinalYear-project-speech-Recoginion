import pyttsx3

engine = pyttsx3.init()

sound = engine.getProperty('voices')
rate = engine.getProperty('rate')


engine.setProperty('rate', rate-50)

#for voice in voices:
engine.setProperty('voice', sound[1].id)

engine.say('The Bogey Beast by Flora Annie Steel')
engine.say("A woman finds a pot of treasure on the road while she is returning from work. Delighted with her luck, she decides to keep it. As she is taking it home, it keeps changing. However, her enthusiasm refuses to fade away.") 
engine.say("The old lady in this story is one of the most cheerful characters anyone can encounter in English fiction. Her positive disposition (personality) tries to make every negative transformation seem like a gift, and she helps us look at luck as a matter of perspective rather than events.")

engine.runAndWait()