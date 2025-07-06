# ✅ 1. Define a class and create object

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display_info(self):
        print(f"👤 Name: {self.name}")
        print(f"📘 Course: {self.course}")


# Creating an object
s1 = Student("Moiz", "Python")
s1.display_info()
