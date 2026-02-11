#students = ["Alice", "Bob", "Charlie", "David", "Eve"]
#state = {"Alaska", "Arizona", "Arkansas", "California", "Colorado"}

students = {"Alice": "Alaska", "Bob": "Arizona", "Charlie": "Arkansas", 
            "David": "California", "Eve": "Colorado"}

print(students["Alice"])

for name in students:
    print(name, students[name])