# ✅ 1. Simple if statement
age = 18
if age >= 18:
    print("✅ You are eligible to vote.")

# ✅ 2. if-else statement
marks = 45
if marks >= 50:
    print("🎉 Passed")
else:
    print("❌ Failed")

# ✅ 3. if-elif-else statement
grade = 85
if grade >= 90:
    print("🌟 Grade: A+")
elif grade >= 80:
    print("🎖️ Grade: A")
elif grade >= 70:
    print("🎓 Grade: B")
else:
    print("📄 Grade: Below B")

# ✅ 4. Nested if
user = "admin"
password = "1234"
if user == "admin":
    if password == "1234":
        print("🔓 Access Granted")
    else:
        print("🔐 Incorrect Password")
else:
    print("⛔ Unknown User")

# ✅ 5. Using logical operators
x = 10
if x > 5 and x < 15:
    print("✅ x is between 5 and 15")

if not x == 20:
    print("❗ x is not 20")

# ✅ 6. Short-hand if
score = 75
print("👍 Good Job") if score >= 70 else print("👎 Try Again")
