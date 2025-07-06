# ✅ 2. Add method to update data

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def update_course(self, new_course):
        self.course = new_course
        print(f"✅ Course updated to: {self.course}")


s2 = Student("Ali", "Java")
s2.update_course("AI")
