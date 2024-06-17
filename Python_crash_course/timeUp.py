from plyer import notification
import time
import pyttsx3

# initialize the text-to-speech engine
engine = pyttsx3.init()

# define the message and voice
message = "It is time to read for one hour!!!"
voice = "english+m3"

# set the voice for the text-to-speech engine
voices = engine.getProperty('voices')
engine.setProperty('voice', voice)

# show the notification
notification.notify(title="Time's Up!", message="Your time is up.", timeout=60)

# print the available voices
voices = engine.getProperty('voices')
for voice in voices:
    print(voice.id)

# speak the message repeatedly for 20 seconds
for i in range(20):
    engine.say(message)
    engine.runAndWait()
    time.sleep(1)
