# 1. Create and write to a file
import os
file = open("names.txt", "w")  # "w" mode = write (overwrite if file exists)
file.write("Hello! I am Abdul Moiz.\n")
file.write("I am a Python Developer.\n")
file.write("I am learning Python.\n")
file.close()
print("✅ File written successfully.")

# 2. Read entire content
file = open("names.txt", "r")  # "r" mode = read
content = file.read()
print("\n📄 File Content:\n", content)
file.close()

# 3. Read line by line
file = open("names.txt", "r")
print("\n📚 Reading line by line:")
for line in file:
    print(line.strip())  # strip() removes newlines
file.close()

# 4. Append to file
file = open("names.txt", "a")  # "a" mode = append
file.write("I am from Pakistan.\n")
file.close()
print("📝 Line appended successfully.")

# 5. Using 'with' (Auto close file)
print("\n🔒 Using 'with' statement:")
with open("names.txt", "r") as file:
    print(file.read())

# 6. Delete a file (Optional — only use if needed)
# if os.path.exists("names.txt"):
#     os.remove("names.txt")
#     print("🗑️ File deleted.")
# else:
#     print("⚠️ File not found.")


# with open("names.txt", "r") as file:
#     print(file.read())
