#!/usr/bin/python3
# try:
#     a = int(input("Enter the number: "))
#     print(f"Multiplication table of {a} is: ")


#     for i in range(1, 11):
#         print(f"{a} X {i} = {(a)*i}")
# except:
#     print("Invalid Input!")


try:
    num = int(input("Enter an Integar: "))
    a = [3, 4, 5]
    print(a[num])
except ValueError:
    print("Number entered is not an integer!")

except IndexError:
    print("Out of range!")
finally:
    print("I must be executed")