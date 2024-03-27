import pyttsx3 as p
import speech_recognition as sr

engine = p.init()

def say(text):
    engine.say(text)
    engine.runAndWait()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio,language="En-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "I Couldn't understand that. Can you repeat it again"

if __name__ == '__main__':
    print('Pycharm')
    say("Hello, I am Paimon A I")

    while True:
        print("Listening...")
        query = takeCommand()
        say(query)