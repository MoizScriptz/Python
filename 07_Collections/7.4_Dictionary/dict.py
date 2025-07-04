#  1. Create a dictionary
student = {
    "name": "Moiz",
    "age": 20,
    "course": "Python",
    "marks": 85
}

print("🎓 Student Dictionary:", student)

#  2. Access a value
print("📌 Student Name:", student["name"])

#  3. Add a new key-value pair
student["city"] = "Lahore"
print("🏙️ Updated with City:", student)

#  4. Update an existing value
student["marks"] = 90
print("📈 Marks Updated:", student)

#  5. Delete a key
del student["age"]
print("❌ Age Removed:", student)

#  6. Use .get() to safely access keys
print("📥 Course:", student.get("course"))
print("📥 Roll Number (Not exist):", student.get("roll_no", "Not Assigned"))

#  7. Loop through dictionary
print("\n🔁 Looping through keys and values:")
for key, value in student.items():
    print(f"{key} ➡️ {value}")

#  8. Dictionary Length
print("📏 Total Fields:", len(student))

#  9. Get all keys and values
print("🔑 All Keys:", student.keys())
print("📦 All Values:", student.values())

#  10. Clear the dictionary
student.clear()
print("🧹 Dictionary Cleared:", student)
