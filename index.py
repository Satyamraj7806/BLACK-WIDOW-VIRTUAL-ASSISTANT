

# Jarvis Voice Assistant


import speech_recognition as sr
import webbrowser 
import pyttsx3
import os 
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
from dotenv import load_dotenv
import pygame


recognizer = sr.Recognizer()
engine = pyttsx3.init()
load_dotenv()
news_api = os.getenv("NEWS_API_KEY")



# def speak(text):
#     engine.say(text)
#     engine.runAndWait()


def speak(text):
        
    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()    
    os.remove('temp.mp3')

def aiprocess(command):
    client = OpenAI(
        api_key= f"{news_api}")

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named 'BLACK WIDOW', skilled in general tasks like Alexa and Google Cloud, and give short responses."},
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message.content

def processcommand(command):
    if "open google" in command.lower():
        speak("Opening Google")
        webbrowser.open ("https://www.google.com")
    elif "open youtube" in command.lower():
        speak("Openingyoutubee")
        webbrowser.open ("https://www.youtube.com")
    elif "open instagram" in command.lower():
        speak("Opening instagram")
        webbrowser.open ("https://www.instagram.com")
    elif "open facebook" in command.lower():
        speak("Opening facebook")
        webbrowser.open ("https://www.facebook.com")
    elif "open wikipidia" in command.lower():
        speak("Opening wikipidia")
        webbrowser.open ("https://www.wikipidia.com")
    elif "play" in command.lower():
        song = command.lower().split("")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in command.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            for articles in articles:
                speak (articles["title"])


    

if __name__ == "__main__":
    speak("Initializing Black Widow...")
    while True:
        try:
            
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            word = recognizer.recognize_google(audio).lower()
            if word in ["jarvis","Black widow", "witch", "widow",  "vision", "sattu", "hello", "hi"]:
                speak("Yes sir")
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=0.3)
                    speak("Listening for command...")
                    audio = recognizer.listen(source, timeout=1, phrase_time_limit=4)
                command = recognizer.recognize_google(audio)
                print(f"You said (command): {command}")
                processcommand(command)

            elif word in ["exit", "quit"]:
                speak("Goodbye!")
                break

            else :
                try :
                    output = aiprocess(command)
                    speak(output)
                except Exception as e:
                    print(f"Can't connect to OpenAI: {e}")
                    speak("Sorry, I couldn't connect to OpenAI.")
            

        except Exception as e:
            print(f"Error: {e}")
    
