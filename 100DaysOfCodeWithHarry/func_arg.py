#!/usr/bin/python3

def average(*numbers):  # numbers is a tuple
    print(type(numbers))
    # print(type(average))
    sum = 0
    for i in numbers:
        sum += i
    print("Average is: ", sum / len(numbers))
    
average(4, 7, 9, 67)


def name(**name):
    print(type(name))
    print("Hello", name["fname"],
name['mname'], name['lname'])
    
name(fname = 'Emmanuel', mname = 'kyrian',
     lname = "James")