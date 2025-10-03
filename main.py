import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

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
            print(command)
        except Exception as e:
            print(e)






 
         