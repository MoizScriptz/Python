# 🧠 Python Functions - README

## 🔹 What are Functions?

Functions in Python are **blocks of reusable code** that perform a specific task. They help in making programs more modular, organized, and easier to maintain.

---

## 🔹 Defining a Function

A function is defined using the `def` keyword.

```python
def function_name(parameters):
    # code block
    return result
```

---

## 🔹 Calling a Function

Once defined, you can call a function by using its name followed by parentheses.

```python
function_name(arguments)
```

---

## 🔹 Function Parameters

- **Positional Parameters**: Parameters passed in order.
- **Default Parameters**: Provide a default value if none is passed.
- **Keyword Arguments**: Parameters passed using `key=value` syntax.
- **Arbitrary Arguments**:
  - `*args`: Accepts variable number of positional arguments.
  - `**kwargs`: Accepts variable number of keyword arguments.

```python
def greet(name="User"):
    print("Hello", name)
```

---

## 🔹 Return Statement

Functions can return values using the `return` keyword.

```python
def add(a, b):
    return a + b
```

---

## 🔹 Lambda (Anonymous) Functions

Lambda functions are small, anonymous functions defined with the `lambda` keyword.

```python
lambda arguments: expression
```

Example:

```python
square = lambda x: x * x
```

---

## 🔹 Scope and Lifetime

- **Local Variables**: Defined inside a function.
- **Global Variables**: Declared outside any function.
- Use `global` keyword to modify global variables inside a function.

---

## 🔹 Docstrings

Document your functions using triple-quoted strings right after the function definition.

```python
def greet():
    """This function greets the user."""
    print("Hello!")
```

---

## ✅ Use Cases

- Code reuse and modularity
- Logic separation and organization
- Handling repetitive tasks

---

## 🔚 Conclusion

Functions are essential building blocks in Python. They make code cleaner, more efficient, and easier to debug and scale.
