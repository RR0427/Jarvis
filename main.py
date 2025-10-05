import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
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
    

if __name__ == "__main__":
    speak(" Initalizing Jarvis ")
    while(True):
                    # Obtain audio from the microphone         

        r = sr.Recognizer()

        print("Recongnizing....")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source)
            command = r.recognize_google(audio)
            if (command.lower() == "jarvis"):
                speak("Yes, How may i help you ?")

                # Listen for commant
                with sr.Microphone() as source:
                    print("jarvis Listening.....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

            processCommand(command)

        except Exception as e:
            print(e)






 
         