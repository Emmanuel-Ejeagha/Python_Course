#!/usr/bin/python3

import random

print("Welcome to my Guess Number Game!")
prompt = input('Do you want to play? "yes" or "no": ').lower()
if prompt != 'yes':
    quit()

range_prompt = input("Type a number: ")

if range_prompt.isdigit():
    range_prompt = int(range_prompt)
    
    if range_prompt <= 0:
        print('Please type a number larger than 0 next time')
        quit()
else:
    print("Please type a number next time")

rand2 = random.randint(0, range_prompt)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please type a number next time")
        continue
    if user_guess == rand2:
        print("You got it!")
        break
    
    
    elif user_guess > rand2:
        print("You are above the number!")
    else:
        print("You are below the number!")

print("You got it in", guesses, "guesses")