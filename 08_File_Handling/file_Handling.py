# ✅ 1. Create and write to a file
file = open("sample.txt", "w")  # "w" mode = write (overwrite if file exists)
file.write("Hello, this is the first line.\n")
file.write("This is the second line.\n")
file.close()
print("✅ File written successfully.")

# ✅ 2. Read entire content
file = open("sample.txt", "r")  # "r" mode = read
content = file.read()
print("\n📄 File Content:\n", content)
file.close()

# ✅ 3. Read line by line
file = open("sample.txt", "r")
print("\n📚 Reading line by line:")
for line in file:
    print(line.strip())  # strip() removes newlines
file.close()

# ✅ 4. Append to file
file = open("sample.txt", "a")  # "a" mode = append
file.write("This is a new line added at the end.\n")
file.close()
print("📝 Line appended successfully.")

# ✅ 5. Using 'with' (Auto close file)
print("\n🔒 Using 'with' statement:")
with open("sample.txt", "r") as file:
    print(file.read())

# ✅ 6. Delete a file (Optional — only use if needed)
# import os
# if os.path.exists("sample.txt"):
#     os.remove("sample.txt")
#     print("🗑️ File deleted.")
# else:
#     print("⚠️ File not found.")
