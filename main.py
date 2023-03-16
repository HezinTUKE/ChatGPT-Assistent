import speech_recognition as sr

from gpt import chatGPT
from answer import say

r = sr.Recognizer()

print("start to speek")

while(True) :
    with sr.Microphone() as micro :
        r.adjust_for_ambient_noise(micro, duration=0.2)

        audio = r.listen(micro)

        try : 
            text = r.recognize_google(audio, language = 'en-US')
            print(text)
            
            if text.lower() == 'stop':
                break

            answerGPT = chatGPT(text)
            say(answerGPT)
        except Exception as e:
            print(e)