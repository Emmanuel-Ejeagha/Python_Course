#!/usr/bin/python3

def factorial(n):
    """returns factorial of n"""
    if(n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n -1)
    
print(factorial(5))
print(factorial(4))
print(factorial(3))
print(factorial(2))
print(factorial(1))

def fibo(n):
    """Return fibonacci series upto n"""
    result = []
    x, y = 0, 1
    while x < n:
       result.append(x)
       x, y = y, x+y
    return result

print("\nFibonacci")
print(fibo(40))