#!/usr/bin/python3

import time
# import os

# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# os.system("python3 --version")

t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour = int(input("Enter hour: (-1 end) "))
print(hour)

while hour != -1:
    if(hour >= 0 and hour < 12):
        print("Good Morning Sir!")
    elif(hour >= 12 and hour < 17):
        print("Good Afternoon Sir!")
    elif(hour >= 17 and hour < 21):
        print("Good Evening Sir!")
    elif(hour >= 21 and hour < 24):
        print("Good Night Sir!")
    else:
        print("Out of time frame!")

    hour = int(input("Enter hour: (-1 end) "))
