#!/usr/bin/python3

# s = {1, 2, 3, 4, 3}
# empty_set = set()
# empty_dict = {}

# print(type(s))
# print(type(empty_set))
# print(type(empty_dict))

s1 = {1, 2, 3, 5, 7}
s2 = {3, 2, 6, 4, 1}
x = s1.union(s2)
print(x)
s1.update(s2)
print(s1, s2)

states1 = {'Alaska', 'Miami', 'Atlanta', 'Texas'}
states2 = {'WDC', 'Chicago', 'Arizona', 'Miami', 'Alaska'}
x = states1.intersection(states2)
print(x)

