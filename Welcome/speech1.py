
import pyttsx3;

engine = pyttsx3.init();
rate = engine.getProperty('rate')


engine.setProperty('rate', rate-65)


engine.say("Good afternoon Everyone");

engine.say("Today I am here to represent my final year project that is SIRI DEVI");

engine.runAndWait() ;