#!/usr/bin/python3
# Tuple

tup = (1,9, 8, 77, 6, 4)
print(type(tup))
print(tup[5])

if 45 in tup:
    print("Yes 45 is in this tuple")
else:
    print("No 45 is not in this tuple")
    
print(tup[0:3])
tup1 = (3, 5, 8)
tup += tup1
print(tup)

states = ('Maimi', 'Chicago', 'NYC', 'Texas', 'Atlanta')
temp = list(states)
temp.append("Georgia")
temp[2] = 'Florida'
states = tuple(temp)
print(states)
