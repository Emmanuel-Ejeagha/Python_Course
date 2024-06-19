#!/usr/bin/python3

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'cherry', 'apple', 'orange', 'berries']

print(f"This is the list of our fruits. {fruits}")
print("The total number of oranges on the list is ", fruits.count('orange'))
print("Find next orange after index 1, another orange is in index ", fruits.index('orange', 1))
fruits.reverse()
print(f"This is the reverse of the fruits list: {fruits}")
fruits.append('guava')
print(f'Appended guava to the list {fruits}')
fruits.sort()
print(f"Sort the list {fruits}")
ppop = fruits.pop()
print(f"popped {ppop}")