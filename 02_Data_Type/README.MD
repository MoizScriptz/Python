
# 🐍 Python Data Types - Summary

Python has various data types built-in by default, used to define the kind of value a variable holds.

---

## 📦 Built-in Data Types

| Category       | Data Types                                                  |
|----------------|-------------------------------------------------------------|
| Text Type      | `str`                                                       |
| Numeric Types  | `int`, `float`, `complex`                                   |
| Sequence Types | `list`, `tuple`, `range`                                    |
| Mapping Type   | `dict`                                                      |
| Set Types      | `set`, `frozenset`                                          |
| Boolean Type   | `bool`                                                      |
| Binary Types   | `bytes`, `bytearray`, `memoryview`                          |
| None Type      | `NoneType`                                                  |

Use `type()` to check the data type:

```python
x = 5
print(type(x))  # <class 'int'>
```

---

## 🔢 Numbers

Python has three numeric types:

- **int**: Whole numbers → `x = 10`
- **float**: Decimal numbers → `y = 3.14`
- **complex**: Complex numbers → `z = 1 + 2j`

```python
a = 1        # int
b = 2.5      # float
c = 3 + 4j   # complex
```

---

## 🔁 Type Casting

Convert one data type to another:

```python
x = int(1.8)        # 1
y = float("2")      # 2.0
z = str(3.5)        # '3.5'
```

Use casting functions:
- `int()`
- `float()`
- `str()`

---

## ✅ Boolean

Booleans represent **True** or **False** values:

```python
a = True
b = False
```

Booleans are often used in condition checking:

```python
print(10 > 5)   # True
print(5 == 5)   # True
print(5 < 3)    # False
```

Python treats the following as **False**:
- `0`
- `""` (empty string)
- `[]`, `{}`, `()`, `None`

Everything else is considered **True**.

---

## 🔤 Strings

Strings are sequences of characters enclosed in single `'` or double `"` quotes.

```python
name = "Alice"
```

### Common String Operations

```python
txt = "Hello World"
print(len(txt))             # 11
print(txt.lower())          # hello world
print(txt.upper())          # HELLO WORLD
print(txt.replace("H", "J"))# Jello World
print("World" in txt)       # True
print(txt[0])               # H
```

Strings are immutable and **indexed**.

---

## 📝 Summary

- Python supports many data types like `str`, `int`, `float`, `bool`
- Use `type()` to identify types
- Use casting to convert between types
- Strings and booleans are used heavily in conditions and output formatting

---

Happy Learning! 🚀
