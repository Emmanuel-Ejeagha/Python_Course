#!/usr/bin/python3
# counts the number of odd and even numbers

odd_numbers = 0
even_numbers = 0

number = int(input("Enter a number or type 0 to stop! "))

while number != 0:
    if number % 2 == 1:
        odd_numbers += 1
    else:
        even_numbers += 1
    
    number = int(input("Enter a number or type 0 to stop! ")) 
print(f"Odd numbers count: {odd_numbers}")
print(f"Even numbers count: {even_numbers}")    
