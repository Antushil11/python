# Dictionary
student = {
    "name": "Antu",
    "city": "chattogram",
    "age": 25,
    "roll": 24
}
print(type(student))
print(student["name"])
print(student)
print(student["city"])

#update

student["city"]="Dhaka"
print(student)

student["favSubject"]="maths"
print(student)

#Remove
student.pop("favSubject")
print(student)

print(student.keys())
print(student.values())
print(student.items())




