#!/usr/bin/python3

def fib(num):
    """ Returns a list of fibonacci series"""
    result = []
    a, b = 0, 1

    while a < num:
        result.append(a)
        a = b
        b = a + b
    return result


i = fib(1000)
print(i)
