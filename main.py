import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "dc38d352f8364b1e9634dd7e88a2b783"

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open insta" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open twitter" in c.lower():
        webbrowser.open("https://x.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r =requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")    
        if r.status_code == 200:
            data = r.json()  # Parse JSON response
            articles = data.get('articles', []) # Get the list of articles
            
            # Loop through articles and print headlines
            for article in articles:
                speak(article['title'])
    

if __name__ == "__main__":
    speak(" Initalizing Jarvis ")

    while(True):
                    # Obtain audio from the microphone         

        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)

                print("Listening....")
                audio = recognizer.listen(source, timeout=6)
            word = recognizer.recognize_google(audio)
            print(f"Heard: {word}")
            if (word.lower() == "jarvis"):
                speak("yes")

                # Listen for commant
                with sr.Microphone() as source:
                    print("jarvis Listening.....")
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source, timeout=6, phrase_time_limit=4)
                    command = recognizer.recognize_google(audio)
                    print(f"Command: {command}")
                    processCommand(command)

        except Exception as e:
            print(e)






 
         