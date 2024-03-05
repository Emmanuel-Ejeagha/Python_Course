import datetime
import time
import pyttsx3

# set up the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english+m3')  # use a female voice

# define the wake-up message
message = "Good morning Boss, it's time to wake up"

# loop forever
while True:
    # get the current time
    now = datetime.datetime.now()

    # check if it's 4am
    if now.hour == 4 and now.minute == 0:
        # speak the wake-up message
        engine.say(message)
        engine.runAndWait()

        # scream for 5 minutes
        for i in range(5 * 60):  # 5 minutes = 300 seconds
            engine.say("Boss, Wake up and read your book!")
            engine.runAndWait()
            time.sleep(1)  # sleep for 1 second

    # sleep for 1 minute before checking the time again
    time.sleep(1 * 60)
