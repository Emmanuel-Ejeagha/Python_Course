#!/usr/bin/python3
print("Welcome to my computer quiz!")

play_prompt = input("Do you want to play? 'yes' or 'no': ").lower()

if play_prompt != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does API stands for? ")
if answer.lower() == "application programming interface":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("WWhat does GPU stands for? ")
if answer.lower()  == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stands for? ")
if answer.lower()  == "ramdom access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does ROM stands for? ")
if answer.lower()  == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does GUI stands for? ")
if answer.lower()  == "graphical user interface":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does CLI stands for? ")
if answer.lower()  == "command line interface":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does PSU stands for? ")
if answer.lower()  == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + "q uestions correct!")
print("you got " + str((score / 7) * 100) + "%.")
