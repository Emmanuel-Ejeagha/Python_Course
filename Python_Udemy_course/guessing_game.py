#!/usr/bin/bash
#Guessing game with different levels


import random

def guessing_game(guess_limit, number):
    random_number = random_randint(1, number)
    try:
        while guess_limit > 0
        guess = int(input("What is your guess? "))
        guess_limit -= 1

        if random_number == guess:
            print("Congrats! you got it right")
            break
        elif guess > number:
            print("Your Guess is out of hand")
            print(f"You have {guess_limit} guess(es) left")


