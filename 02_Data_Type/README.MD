# Built-in Data Types
#### In programming, data type is an important concept.

#### Variables can store data of different types, and different types can do different things.

#### Python has the following data types built-in by default, in these categories:

## 🧾 Python Data Types

| Data Type Category | Example Types                         |
|:-------------------|:--------------------------------------|
| Text Type           | `str`                                |
| Numeric Types       | `int`, `float`, `complex`            |
| Sequence Types      | `list`, `tuple`, `range`             |
| Mapping Type        | `dict`                               |
| Set Types           | `set`, `frozenset`                   |
| Boolean Type        | `bool`                               |
| Binary Types        | `bytes`, `bytearray`, `memoryview`   |
| None Type           | `NoneType`                           |

## Setting the Data Type
#### In Python, the data type is set when you assign a value to a variable:
## 🧠 Python Variable Types with Examples

| Code Example                                 | Data Type     |
|:---------------------------------------------|:--------------|
| `x = "Hello World"`                          | `str`         |
| `x = 20`                                     | `int`         |
| `x = 20.5`                                   | `float`       |
| `x = 1j`                                     | `complex`     |
| `x = ["apple", "banana", "cherry"]`          | `list`        |
| `x = ("apple", "banana", "cherry")`          | `tuple`       |
| `x = range(6)`                               | `range`       |
| `x = {"name" : "John", "age" : 36}`          | `dict`        |
| `x = {"apple", "banana", "cherry"}`          | `set`         |
| `x = frozenset({"apple", "banana", "cherry"})` | `frozenset` |
| `x = True`                                   | `bool`        |
| `x = b"Hello"`                               | `bytes`       |
| `x = bytearray(5)`                           | `bytearray`   |
| `x = memoryview(bytes(5))`                   | `memoryview`  |
| `x = None`                                   | `NoneType`    |

## Setting the Specific Data Type
#### If you want to specify the data type, you can use the following constructor functions:
## 🧠 Python Variable Constructors

| Code Example                                       | Data Type     |
|:--------------------------------------------------|:--------------|
| `x = str("Hello World")`                          | `str`         |
| `x = int(20)`                                     | `int`         |
| `x = float(20.5)`                                 | `float`       |
| `x = complex(1j)`                                 | `complex`     |
| `x = list(("apple", "banana", "cherry"))`         | `list`        |
| `x = tuple(("apple", "banana", "cherry"))`        | `tuple`       |
| `x = range(6)`                                    | `range`       |
| `x = dict(name="John", age=36)`                   | `dict`        |
| `x = set(("apple", "banana", "cherry"))`          | `set`         |
| `x = frozenset(("apple", "banana", "cherry"))`    | `frozenset`   |
| `x = bool(5)`                                     | `bool`        |
| `x = bytes(5)`                                    | `bytes`       |
| `x = bytearray(5)`                                | `bytearray`   |
| `x = memoryview(bytes(5))`                        | `memoryview`  |

## Random Number
### Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:


## 🎲 Generate a Random Number in Python

```python
import random
print(random.randint(1, 10))

```
## Boolean Values
#### In programming you often need to know if an expression is True or False.
#### You can evaluate any expression in Python, and get one of two answers, True or False.
#### When you compare two values, the expression is evaluated and Python returns the Boolean answer:

#### Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
```python
x = 2543
print(isinstance(x,int))