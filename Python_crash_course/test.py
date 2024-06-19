# x = 42
# print(type(x))
#
# y = 0.54
# print(type(y))
#
# # def f(x):
# #     return x + 1
# # print(type(f))
#
# import math
# print(type(math))
#
# class Robot:
#     pass
#  # f __name__ == "__main__":
#  #    x = Robot()
#  #    y = Robot()
#  #    y2 = y
#  #    print(y == y2)
#  #    print(y== x)
# #
#
# x = Robot()
# Robot.brand = 'Grace'
# print(x.brand)
# print('hello')
# y = Robot()
# Robot.brand = "Ken"
# print(y.brand)
# print(y.__dict__)
# print(x.__dict__)
# print(Robot.__dict__)
#
# def f(x):
#     f.counter = getattr(f, 'counter', 0) + 1
#     return "Monty Python"
# for i in range(10):
#     f(1)
# print(f.counter)
#
# def sayHi(obj):
#     print("Hi, I am " + obj.name + "!")
# class Robot:
#     pass
# x = Robot()
# x.name = "Javis"
# i = sayHi(x)
# # print(i)
# f = f.open('py', w)j

class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """
    pass

b = Base()
u = User()
print(u.id)