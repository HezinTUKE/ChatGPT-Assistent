import speech_recognition as sr

from gpt import chatGPT
from answer import say

r = sr.Recognizer()

print("start to speek")

with sr.Microphone() as micro :
    r.adjust_for_ambient_noise(micro, duration=0.2)

    audio = r.listen(micro)
    
    text = r.recognize_google(audio, language = 'en-US')

    print(text)

    answerGPT = chatGPT(text)

    say(answerGPT)