# create a json file
import json

college = {
    "college": "Engineering College",
    "objectives": "mastering Electrical and Computer Engineering",
    "departments": {
        "dept1": "Electrical",
        "dept2": "Computer"
    },
    "years": [
        "year 1",
        "year 2",
        "year 3",
        "year 4"
    ],
    "numbers": [1, 2, 3, 4],
    "ID": [10, 20, 30, 40]
}
# create a json file
write = json.dump(college, open("college.json", "w"))

# read a json file
new_college = json.load(open("college.json", "r"))
print(new_college)