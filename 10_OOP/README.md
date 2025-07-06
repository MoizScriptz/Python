# 🧱 Python Object-Oriented Programming (OOP) - README

## 🔹 What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of **"objects"**, which can contain **data** (attributes) and **code** (methods).

---

## 🔹 Key Concepts of OOP

| Concept       | Description                                                       |
|---------------|-------------------------------------------------------------------|
| **Class**     | A blueprint for creating objects                                  |
| **Object**    | An instance of a class                                            |
| **Attributes**| Variables associated with a class or object                       |
| **Methods**   | Functions defined inside a class                                  |
| **Encapsulation** | Bundling data and methods that operate on the data            |
| **Inheritance**   | Mechanism for creating a new class from an existing class     |
| **Polymorphism**  | Ability to use a common interface for different data types    |
| **Abstraction**   | Hiding internal implementation and showing only functionality |

---

## 🔹 Defining a Class

```python
class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}")
```

---

## 🔹 Creating an Object

```python
obj = MyClass("Alice")
obj.greet()
```

---

## 🔹 Constructor (`__init__`)

A special method that is automatically called when a class is instantiated.

---

## 🔹 `self` Keyword

Refers to the instance of the class. Used to access variables and methods inside the class.

---

## 🔹 Inheritance

One class inherits the properties and methods of another.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")
```

---

## 🔹 Method Overriding

You can override a parent class method in a child class.

```python
class Dog(Animal):
    def speak(self):
        print("Dog barks")
```

---

## 🔹 Encapsulation Example

```python
class Person:
    def __init__(self, name):
        self.__name = name  # private variable

    def get_name(self):
        return self.__name
```

---

## 🔹 Polymorphism Example

```python
class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Bark")

for animal in (Cat(), Dog()):
    animal.speak()
```

---

## ✅ Use Cases

- Designing real-world models in code
- Building scalable and reusable code
- Useful in large-scale software projects

---

## 🔚 Conclusion

OOP in Python provides a clean and modular structure to your code. It encourages reuse, inheritance, and encapsulation, making it a powerful tool for building robust applications.
