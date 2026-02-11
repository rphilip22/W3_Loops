#Dictionary example

#students = ["Alice", "Bob", "Charlie", "David", "Eve"]
#state = {"Alaska", "Arizona", "Arkansas", "California", "Colorado"}

#students = {"Alice": "Alaska", "Bob": "Arizona", "Charlie": "Arkansas", 
#            "David": "California", "Eve": "Colorado"}

#print(students["Alice"])

#for name in students:
#    print(name, students[name])


#list of dictionaries example

students = [
    {"name": "Alice", "state": "Alaska", "gender": "Female"},
    {"name": "Bob", "state": "Arizona", "gender": "Male"},
    {"name": "Charlie", "state": "Arkansas", "gender": "Male"},
    {"name": "David", "state": "California", "gender": "Male"},
    {"name": "Eve", "state": "Colorado", "gender": "Female"},
    {"name": "Colin", "state": "Connecticut", "gender": None}
]

for student in students:
    print(student["name"], student["state"], student["gender"])