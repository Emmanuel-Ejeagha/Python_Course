#!/usr/bin/python3
# This script prints the largest number

largest_number = -999999999
number = int(input("Enter a number or type -1 to stop: "))

while number != -1:
    if number > largest_number:
        largest_number = number

    number = int(input("Enter a number or type -1 to stop: "))
print(f"The Largest number is {largest_number}")
