#init
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)
print(person.name)  # Output: John
print(person.age)  # Output: 30

#call
class Example:
    def __call__(self, *args, **kwargs):
        print("Called")

example = Example()
example()  # Output: Called

#str
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

point = Point(4, 5)
print(str(point))  # Output: Point(4, 5)
