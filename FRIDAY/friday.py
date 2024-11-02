import pyttsx3                       #used for converting text to speech
import speech_recognition as sr      #used for capturing voice
import webbrowser as wb              #used for accessing URLs in web browser directly through PYTHON
import datetime as dt                #used for handling dates,time intervals
import pyjokes as py                 #used for random technical jokes
import time

def speech_text():
    while True:
        recognizer=sr.Recognizer()
        with sr.Microphone() as source:
            print("FRIDAY INITIALIZED...")

            recognizer.adjust_for_ambient_noise(source)   #Background noise of source is to be removed.
            audio=recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)  #Audio convert into text data and assigned to a variable
            return data

        except sr.UnknownValueError:            #Exceptional handling for no input as voice
            print("Not Understood")

def text_speech(x):
    engine=pyttsx3.init()                       #init is a class containing functions.

    voices=engine.getProperty('voices')         #used to get a voice of female/male
    engine.setProperty('voice',voices[1].id)    #Index: 0-Male ; 1-Female ;
    
    rate=engine.getProperty('rate')             #used to handle the speed of Friday
    engine.setProperty('rate',150)              #150 words per minute

    engine.say(x)
    engine.runAndWait()

if __name__=='__main__':                        #used to break codes and run as per our needs

    #if speech_text().lower() == "friday" :      #necessary to do it lowercase & activate the program.
        while True: 
            data1=speech_text().lower()
            
            if "daddy's home" in data1:
                reply="Welcome home sir."
                text_speech(reply)
                
            elif "your name" in data1:
               name= " my name is Friday."
               text_speech(name)
            
            elif "are you doing" in data1:
               over= " Im doing excellent."
               text_speech(over)
        
            elif "time" in data1:
               time=dt.datetime.now().strftime("%I%M%p")    #strftime is used to limit time output to hours/min/sec without it tells us the entire time.
               text_speech(time)

            elif "youtube" in data1:
               wb.open("https://www.youtube.com/")         #open is a function which is used to open any webpage.

            elif "google" in data1:
               wb.open("https://www.google.com/")         #open is a function which is used to open any webpage.

            elif "spotify" in data1:
               wb.open("https://www.spotify.com/")         #open is a function which is used to open any webpage.
            
            elif "joke" in data1:
                jokes=py.get_joke(language="en")
                print(jokes)
                text_speech(jokes)

            elif "bye" in data1:
                text_speech("Have a great day sir")
                break

else:
    print("Thanks")
