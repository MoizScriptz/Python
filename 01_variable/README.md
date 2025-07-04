
# 🐍 Python Variables - Summary

Variables in Python are containers for storing data values. They are fundamental building blocks in any Python program.

---

## 📌 What is a Variable?

A **variable** is a name that refers to a value stored in memory.

```python
x = 5
name = "Alice"
```

- `x` and `name` are variables.
- `5` is an integer value.
- `"Alice"` is a string value.

---

## 🧠 Key Rules for Variables

| Rule                         | Description                                                   |
|-----------------------------|---------------------------------------------------------------|
| **Case-Sensitive**          | `age`, `Age`, and `AGE` are different variables               |
| **Start with Letter/Underscore** | Variable names must start with a letter or underscore `_` |
| **No Special Characters**   | Cannot include symbols like `@`, `$`, `%`, etc.               |
| **No Reserved Words**       | Cannot use Python keywords like `class`, `def`, etc.          |

---

## 🔤 Variable Types

Python automatically assigns the data type based on the value:

```python
x = 10            # int
y = 3.14          # float
name = "Alice"    # str
is_valid = True   # bool
```

Use `type()` function to check type:

```python
print(type(x))  # <class 'int'>
```

---

## ♻️ Changing Values

Variables can be reassigned anytime:

```python
x = 10
x = "Now a string"
```

---

## 🪄 Multiple Assignments

You can assign multiple variables in one line:

```python
a, b, c = 1, 2, 3
```

Or assign the same value to multiple variables:

```python
x = y = z = 100
```

---

## 🔄 Variable Casting

Convert one type to another:

```python
x = str(3)      # '3'
y = int("4")    # 4
z = float("5")  # 5.0
```

---

## 📝 Summary

- Variables store data values.
- They are dynamically typed.
- Naming rules must be followed.
- Variables can be reassigned and cast into other types.

---

Happy Coding! 🚀
