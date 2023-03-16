import pyttsx3
engine = pyttsx3.init()

def say(answer : str):
    engine.setProperty('rate', 150)
    engine.say(answer)
    engine.runAndWait()