from plyer import notification
import time
import pyttsx3

engine = pyttsx3.init()
title = 'Notification Title'
message = 'It is time to read for one hour'
timeout = 120   # seconds
voice = 'english+m3'

# show the notification
notification.notify(title=title, message=message, timeout=timeout)
engine.say(message)
# wait for the timeout to finish
time.sleep(timeout)
