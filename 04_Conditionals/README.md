# 📘 Python Conditionals - README

## 🔹 What are Conditionals?

Conditionals in Python are **control flow statements** that allow a program to make decisions and execute specific blocks of code depending on whether certain conditions are met.

They are based on **Boolean logic**: expressions that evaluate to `True` or `False`.

---

## 🔹 Types of Conditional Statements

### ✅ `if` Statement  
Executes a block of code **only if** a condition is true.

```python
if condition:
    # code block
```

---

### ✅ `if-else` Statement  
Provides an **alternative block** of code if the condition is false.

```python
if condition:
    # code block if true
else:
    # code block if false
```

---

### ✅ `if-elif-else` Statement  
Used to check **multiple conditions** sequentially, executing the first block that is true.

```python
if condition1:
    # code block
elif condition2:
    # code block
else:
    # default code block
```

---

## 🔹 Logical Operators in Conditions

| Operator | Meaning                        | Example                          |
|----------|--------------------------------|----------------------------------|
| `and`    | True if **both** conditions are true     | `x > 10 and x < 20`             |
| `or`     | True if **at least one** condition is true | `x > 10 or x == 5`           |
| `not`    | Inverts the truth value        | `not x > 10`                     |

---

## 🔹 Comparison Operators

| Operator | Description              | Example             |
|----------|--------------------------|---------------------|
| `==`     | Equals                   | `x == y`            |
| `!=`     | Not equal                | `x != y`            |
| `>`      | Greater than             | `x > y`             |
| `<`      | Less than                | `x < y`             |
| `>=`     | Greater than or equal to | `x >= y`            |
| `<=`     | Less than or equal to    | `x <= y`            |

---

## 🔹 Nested Conditionals

You can place an `if` or `else` block **inside another `if` statement**.

```python
if condition1:
    if condition2:
        # nested block
```

---

## 🔹 Ternary (One-line) Conditional

Python supports **one-line conditional expressions**:

```python
value_if_true if condition else value_if_false
```

---

## ✅ Use Cases

- Decision-making based on user input or system state.
- Branching logic in algorithms.
- Validating data or conditions.

---

## 🔚 Conclusion

Conditionals are fundamental to programming logic. They enable your Python programs to respond dynamically to different inputs, making your code more intelligent and interactive.
