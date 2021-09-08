import pyttsx3 #pip install pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def speak(Text):
    print("      ")
    print(f"April : {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("    ")

speak("Hi Don't forgot to subscribe")