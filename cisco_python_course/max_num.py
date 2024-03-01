#!/usr/bin/python3
# this program prints the largest number

try:
    print("Enter three integers and i will tell you the maximum")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))

    largest_num = max(num1, num2, num3)
    print(largest_num)

except(ValueError):
    print("The input must be an integar")

