info = {
    'First_name': 'Harry',
    'Middle_name': 'Kyrian',
    'Last_name': 'Bren',
    'Age': 26,
    'Occupation': 'Software Engineer',
    'Status': 'Single'
}

# print(info.keys())
# print(info.values())

# for key in info.keys():
#     print(f"The value corresponding to the {key} is {info[key]}")


print(info.items())
for key, value in info.items():
    print(f"The value corresponding to the '{key}' is {value}")
    
# Methods in Dictionary
emp_perfm1 = {
    121: 60, 123: 69, 128: 79, 134: 87
}
emp_perfm2 = {
    122: 80, 124: 69, 125: 80,  130: 70
}

emp_perfm1.update(emp_perfm2)
print(emp_perfm1)
# emp_perfm1.clear()
print(emp_perfm1)
emp_perfm1.popitem()
print(emp_perfm1)
del emp_perfm1(121)
print(emp_perfm1)
