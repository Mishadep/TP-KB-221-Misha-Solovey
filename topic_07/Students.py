class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

students = [Student("Іван", 21), Student("Петро", 20), Student("Марія", 22)]

sorted_students = sorted(students, key=lambda x: x.name)

for student in sorted_students:
    print(f"Ім'я: {student.name}, Вік: {student.age}")
