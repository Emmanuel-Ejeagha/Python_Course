def fib1(n):

    """Solves fibonacci of n"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


def fib2(n):

    """This function multiplies the fibonacci of n"""
    a, b = 1, 2
    while a < n:
        print(a, end=", ")
        a, b = b, a+b
    print()

if __name__ == "__main__":
        import sys
        n = int(sys.argv[1])
        print(fib1(n))
        fib2(n)
