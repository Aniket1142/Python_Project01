#text to speech project 1.0

import pyttsx3

text_speech = pyttsx3.init()

voices = text_speech.getProperty('voices')
text_speech.setProperty('voice', voices[1].id)

while True:
    a= input("Enter your text here - ")       
    if a == "close":
        text_speech.say('Bye, Have a nice day!')
        break
    text_speech.say(a)
    text_speech.runAndWait()


