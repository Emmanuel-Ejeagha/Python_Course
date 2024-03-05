file = "C:\\Users\\DELL\\OneDrive\\Desktop\\learning_python.txt"
with open(file) as data:
    contents = data.readlines()

lines = ""
for content in contents:
    lines += content
print(lines).
print(lines)
print(lines)


message = "Can you take good care of me?"
m = message.replace('me', 'house and my kids')
print(m)