import speech_recognition as sr
from datetime import datetime
start_time=datetime.now()
r = sr.Recognizer()
m = sr.Microphone()
try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.record(source)
        print("Got it! Now to recognize it...")
        text=" "
        try:
            value = r.recognize_google(audio)
            #value=r.recognize_sphinx(audio)
            #value=r.recognize_bing(audio)

            if str is bytes:
                print(u"You said: {}".format(value).encode("utf-8"))
                text="{}".format(value).encode("utf-8")
            else:
                print("You said: {}".format(value))
                text="{}".format(value)
            end_time=datetime.now()
            print(f"you said: {text}")
            print(f"execution time : {end_time-start_time}")
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass