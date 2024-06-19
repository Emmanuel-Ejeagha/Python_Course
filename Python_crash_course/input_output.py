# name = 'emma'
# age = 18
# print(f"My name is {name.title()}, I am {age} years old")
#
#
# name, age = 'jeff', 25
# print("my name is {}, I am {} years old" .format(name.title(), age))
#
# print(repr(name))
# s = 'Hello World'
# print(repr(s))


# yes_votes = 42_572_654
# no_votes = 43_132_495
# percentage = yes_votes / (yes_votes + no_votes)
#
# print(F"{yes_votes:,.0f} YES votes {percentage:2.2%}")
# x = 10*3.25
# y = 200*200
# s = 'Python Programming language'
# print(s.find("m"))
# print(s.count('P'))
# print(s[:])
# print(file(3**2))
#
# print(repr((x, y, ('spam', 'eggs'))))
#
# import math
# print(f"The value of pi is approximately {math.pi:.3f}.")
# print("Table              Price(#)")
# table = {'Yam': 1000, 'Rice': 3000, 'tomatoes': 600, 'meat': 1_500}
# for food, amount in table.items():
#     print(f"{food:10} ==> {amount:10d}")
# print("-------------------------------------")
# print(f'Total = {sum(table.values()):17d}')

# animals = 'dogs'
# print(f"This neighbourhood is full of {animals}")
# print(f"This neighbourhood is full of {animals!r}")
# print(f"This neighbourhood is full of {animals!s}")
# print(f"This neighbourhood is full of {animals!a}")

# bugs ='spiders'
# count = 7
# area = 'Bed Room'
#
# print(f"Debugging {bugs=} {count=} {area=}")

# print("{}  {}".format('Foods', 'prices'))
#
# for x in range(1, 11):
#     print("{0:2d} {1:3d} {2:4d}".format(x, x*x, x*x*x))
#
# import math
# print("The value of pi is approximately %5.3f" %math.pi)
#
# print("12".zfill(3))
# print("-34.43".zfill(3))

# f = open('workfile.txt', 'w', encoding="utf-8")
#
# with open('workfile.txt', encoding="utf-8") as f:
#     read_data = f.read()
#
# # We can check that the file has been automatically closed.
# print(f.closed)
#
# f.read()
# "This is the first line of the file.\n"
# f.read()

# filename = 'workfile.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# pi_fileing = ''
# for line in lines:
#     pi_fileing += line.fileip()
# print(f"{pi_fileing[:52]}...")
# print(len(pi_fileing))

# with open('workfile.txt') as file:
#     content = file.read()
# print(content)
# print("hi")
#
# with open('workfile.txt') as file:
#     content = file.read()
# print(content.lfileip())
# print("hello")
#
#
# with open('workfile.txt') as file:
#     contents = file.read()
# print(contents.fileip())
# a = 'C:\\Users\\DELL\\OneDrive\\Desktop\\file.txt'
# with open(a) as f:
#     cont1 = f.readline()
#     cont = f.read()
# print(cont)
# print(cont1)

# a = 'C:\\Users\\DELL\\OneDrive\\Desktop\\file.txt'
# with open(a) as file:
#      for line in file:
#          print(line.rstrip())
#
# print()
#
# b = 'C:\\Users\\DELL\\OneDrive\\Desktop\\py.txt'
# with open(b) as text:
#     for lines in text:
#         print(lines)

# c = 'C:\\Users\\DELL\\OneDrive\\Desktop\\file.txt'
# with open(c) as d:
#     lines = d.readlines()
#
# for line in lines:
#     print(line.fileip())

# path = 'C:\\Users\\DELL\\OneDrive\\Desktop\\file.txt'
# with open(path) as file:
#     lines = file.readlines()
#
# file_len = ''
# for line in lines:
#     file_len += line.rstrip()
#
# print(file_len)
# print(len(file_len))

path = 'C:\\Users\\DELL\\OneDrive\\Desktop\\file.txt'
with open(path) as file:
    lines = file.readlines()
    
file_string = ''
for line in lines:

    file_string += line.strip()

check = input("Enter a programming language and i will check if it is in the file: ")
if check in file_string:
    print(f"{check.title()} is a in the file")
else:
    print(f"{check.title()} is not in the file")