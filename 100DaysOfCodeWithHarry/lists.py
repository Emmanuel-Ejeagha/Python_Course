#!/usr/bin/python3
# lists playground

num1 = [23, 45, 54, 67,32, 34, 20]

print(num1)
num1[2] = 34
print(num1)
num1.append(12)
print(num1)
num1.insert(3, 50)
print(num1)
num1.sort()
print(num1)
num1.reverse()
print(num1)
print(num1.index(67))
print(num1)
print(num1.count(34))
num2 = [1, 3, 5, 7, 8, 43]
merge = num1 + num2
print(merge)
merge.sort()
print(merge)