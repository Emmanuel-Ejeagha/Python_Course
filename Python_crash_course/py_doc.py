# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', int(n//x))
#             break
#
#     else:
#         # loop through without finding a factor
#         print(n, "is a prime number")
# #
# for i in list(range(10, -1, -2)):
#     print(i)
# a = ['mary', 'ken', 'emma', 'uche', 'ike']
# for i in range(len(a)):
#     print(i, a[i].title(), "is a member of this group")
# print(sum(range(6)))
def httpError(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Request not found"
        case 408:
            return "I'm a teapot!"
        case _:
            return "Please check your internet connection"
# x = httpError(8)
# print(x)

def error(score):
    match score:
        case 80 | 90 | 100:
            return "You scored 'A' in this course!"
        case 60 | 70:
            return "You scored 'B' in this course"
        case 40 | 50:
            return "You scored 'C' in this course"
        case _:
            return "You have failed and you must rewrite this exam"

# i = error(9)
# print(i)

def fib(n):
    """Print a fibonacci of a number  up to n"""
    a, b = 3, 4
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    #print()

x = fib(505)
# print(x)

def fib1(n):
    """Prints fibonacci of numbers"""
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
        return result
