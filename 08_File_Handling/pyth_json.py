import json

student_data = [
    {
        "name": "Abdul Moiz",
        "age": 20,
        "city": "Lahore",
        "contact": "0326-0107654"
    }
]

# 1. Write JSON data to a file
with open("student_data.json", "w") as file:
    json.dump(student_data, file)
    print("✅ JSON data written to file successfully.")

# 2. Read JSON data from a file
with open("student_data.json", "r") as file:
    data = json.load(file)
    print("\n📄 JSON Data Read from File:")
    print(data)

# 3. Append new data to the JSON file
with open("student_data.json", "r") as file:
    data = json.load(file)


new_data = {"name": "Ali",
            "age": 22,
            "city": "Karachi",
            "contact": "0333-1234567"
            }
data.append(new_data)

with open("student_data.json", "w") as file:
    json.dump(data, file)
    print("\n📝 New data appended to JSON file successfully.")

# 4. Read the updated JSON data
with open("student_data.json", "r") as file:
    updated_data = json.load(file)
    print("\n📄 Updated JSON Data:")
    print(updated_data)
