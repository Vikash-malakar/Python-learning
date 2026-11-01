# Day 10: JSON and File Handling

import json

# 1. Python Dictionary

student = {
    "name": "Vikash",
    "age": 22,
    "course": "Python",
    "skills": ["Python", "Django", "AI"]
}


# 2. Convert Dictionary into JSON

json_data = json.dumps(student, indent=4)

print("JSON Data:")
print(json_data)


# 3. Save JSON into File

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON File Created!")


# 4. Read JSON File

with open("student.json", "r") as file:
    data = json.load(file)

print("Student Details:")
print(data)


# 5. Access JSON Values

print("Name:", data["name"])
print("Age:", data["age"])
print("Course:", data["course"])


# 6. Update JSON Data

data["age"] = 23
data["skills"].append("Machine Learning")


# 7. Save Updated Data

with open("student.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON Updated Successfully!")
print("vikash !!!!!!!!!!!!!!!!!!!!!!!!!!!!!")