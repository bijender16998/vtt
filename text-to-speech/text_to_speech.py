import pyttsx3
engine = pyttsx3.init()
try:
    while True:
        text=input("enter some text..\n")
        try:
            engine.say(text)
            engine.setProperty('rate', 100)
            engine.runAndWait()
        except Exception as e:
            print(e)
            break
except KeyboardInterrupt:
    pass



