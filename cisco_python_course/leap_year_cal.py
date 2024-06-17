#!/usr/bin/python3
# This script calculates the leap year

year = int(input("Enter a year: "))
if year < 1582:
    print("Not within Gregorian calendar")
else:
    if year % 4 != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap Year!")
    elif year % 400 != 0:
        print("Common year")
    else:
        print("Leap year")
