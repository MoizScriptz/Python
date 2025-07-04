# 🔁 Python Loops - README

## 🔹 What are Loops?

Loops are used in Python to **execute a block of code repeatedly**. They help in reducing code duplication and automating repetitive tasks.

---

## 🔹 Types of Loops in Python

### ✅ `for` Loop

Used to iterate over a sequence like list, tuple, dictionary, set, or string. Executes once for each item.

```python
for item in iterable:
    # code block
```

---

### ✅ `while` Loop

Executes a block of code **as long as** the condition is `True`.

```python
while condition:
    # code block
```

---

## 🔹 Loop Control Statements

| Statement   | Description                                       | Syntax Example           |
|-------------|---------------------------------------------------|---------------------------|
| `break`     | Exits the loop completely                         | `if condition: break`     |
| `continue`  | Skips the current iteration and continues the next| `if condition: continue`  |
| `pass`      | Does nothing, used as a placeholder               | `if condition: pass`      |

---

## 🔹 `range()` Function

Commonly used with `for` loops to generate a sequence of numbers.

```python
for i in range(5):
    # executes 5 times (0 to 4)
```

---

## 🔹 Nested Loops

Loops inside loops are called **nested loops**. Useful for multi-dimensional data structures like matrices or grids.

```python
for i in range(3):
    for j in range(2):
        # nested block
```

---

## 🔹 Looping Through Collections

- **Lists/Tuples**:

```python
for item in my_list:
    # do something
```

- **Dictionaries**:

```python
for key, value in my_dict.items():
    # do something
```

- **Strings**:

```python
for char in my_string:
    # process character
```

---

## ✅ Use Cases

- Iterating over data structures
- Automating tasks
- Processing files or user input
- Generating sequences

---

## 🔚 Conclusion

Loops are a fundamental tool for automation and repetition in Python. Mastering loops allows for efficient and clean coding practices.
