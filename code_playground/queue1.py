#!/usr/bin/python3
from collections import deque

queue = deque(['Emma', 'Jerry', 'Mercy', 'Faith', 'Kenny'])
queue.append('Theophilus')
print(queue)
queue.append('Daniel')
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)


# List comprehension
# First Example

squares = []
for x in range(20):
    squares.append(x**2)
print(squares)

# Second Examplehird example, more concise and readable
squares1 = list(map(lambda x: x**2, range(10)))
print(squares1)

# T
squares_num = [x**2 for x in range(10)]
print(squares_num)