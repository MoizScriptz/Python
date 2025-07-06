# ✅ 3. Inheritance (Parent → Child)

class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"🙋 Person: {self.name}")


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def show_details(self):
        self.show()
        print(f"💰 Salary: {self.salary}")


e1 = Employee("Areeba", 50000)
e1.show_details()
