# ✅ 1. For loop (with range)
print("📌 Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

# ✅ 2. While loop
print("\n📌 While loop example:")
x = 1
while x <= 5:
    print(x)
    x += 1

# ✅ 3. Loop through a list
fruits = ["apple", "banana", "mango"]
print("\n🍎 Fruits in the list:")
for fruit in fruits:
    print(fruit)

# ✅ 4. Loop through a dictionary
student = {"name": "Moiz", "age": 20, "course": "Python"}
print("\n📘 Student Info:")
for key, value in student.items():
    print(f"{key}: {value}")

# ✅ 5. Break statement
print("\n⛔ Stop at 3:")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# ✅ 6. Continue statement
print("\n🚫 Skip 3:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# ✅ 7. Nested loop
print("\n📊 Multiplication Table (2 to 4):")
for i in range(2, 5):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")
    print("-----")
