#!/usr/bin/python3

name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

answer = input("You are on a cross road, it has come to an end and you can "
               "choose left or right? ").lower()
if answer == "left":
    answer = input("You come to a river, you walk around it or swim across it. "
                   "options 'walk' or 'swim': " )
    if answer == "swim":
        print("There are sharks in the water and they attacked you!")
    elif answer == "walk":
        print("You have no drinking water and you have exhausted your strength!")
    else:
        print("Not a valid option. You lose.!")
        
elif answer == "right":
    answer = ("You come to a bridge, it looks woobly, do yo want to croos it or "
              "head back: 'cross' or 'back'? ")
    if answer == 'cross':
        print("You are at the bridge but there are tax collectors. "
              "Do you want to pay to pay task: (yes or no): ")
        if answer == 'yes':
            print("")
        elif answer == 'no':
            print("")
        else:
            pass
            
    elif answer == 'back':
        print("There are predators, you lose!")
    
else:
    print("Not a valid option. you lose")
    
print("Thank you for playing!")