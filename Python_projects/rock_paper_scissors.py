#!/usr/bin/python3
# This rock, paper, scissors game
import random

user_wins = 0
computer_wins = 0

options =["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock, Paper, Scissors or Q to quit. ").lower()
    if user_input == "q":
        break
        
    if user_input not in options:
        print("Please type the correct input")
        continue
    randon_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    comp_pick = options[randon_number]
    print("Computer picked", comp_pick + ".")
    
    if user_input == 'rock' and comp_pick == 'scissors':
        print("You won!")
        user_wins += 1
        continue
        
    elif user_input == 'paper' and comp_pick == 'rock':
        print("You won!")
        user_wins += 1
        continue
    
    elif user_input == 'scissors' and comp_pick == 'paper':
        print("You won!")
        user_wins += 1
        continue
    
    else:
        print("You lost!")
        computer_wins += 1  

print("You won", user_wins, "times.")
print("The computer wins", computer_wins, "times.")
print("Gooodbye!")