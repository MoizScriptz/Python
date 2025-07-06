# 📂 Python File Handling - README

## 🔹 What is File Handling?

File handling in Python allows you to **create**, **read**, **write**, and **delete files**. It is used to interact with external files like `.txt`, `.csv`, etc.

---

## 🔹 Opening a File

Use the `open()` function to access a file.

```python
open("filename", "mode")
```

### File Modes:

| Mode | Description                      |
|------|----------------------------------|
| `'r'` | Read (default)                   |
| `'w'` | Write (overwrite)                |
| `'a'` | Append                           |
| `'x'` | Create new file                  |
| `'b'` | Binary mode                      |
| `'t'` | Text mode (default)              |

---

## 🔹 Reading a File

```python
file = open("file.txt", "r")
content = file.read()
file.close()
```

Other methods:
- `read()`: Reads entire file
- `readline()`: Reads one line
- `readlines()`: Reads all lines into a list

---

## 🔹 Writing to a File

```python
file = open("file.txt", "w")
file.write("Hello, World!")
file.close()
```

- Use `'a'` mode to append without overwriting.
- `'w'` mode will **erase existing content**.

---

## 🔹 Using `with` Statement

Automatically handles closing of files.

```python
with open("file.txt", "r") as file:
    content = file.read()
```

---

## 🔹 Working with Binary Files

Use `'rb'` or `'wb'` for binary reading or writing.

---

## 🔹 Checking File Existence

Use the `os` module to check or remove files.

```python
import os

if os.path.exists("file.txt"):
    print("File exists")
else:
    print("File does not exist")
```

---

## 🔹 Deleting a File

```python
import os
os.remove("file.txt")
```

Use `os.rmdir("foldername")` to remove a folder.

---

## ✅ Use Cases

- Reading configuration files
- Logging application data
- Data persistence (e.g., saving user input)
- Import/export data from CSVs or JSON

---

## 🔚 Conclusion

Python file handling is a powerful tool for managing external data. Using the correct modes and best practices (like `with` statement) ensures safety and reliability.
