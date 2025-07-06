# ✅ 1. Basic Function
def greet():
    print("👋 Hello! Welcome to Python functions.")


greet()

# ✅ 2. Function with parameters


def greet_user(name):
    print(f"👤 Hello, {name}!")


greet_user("Moiz")

# ✅ 3. Function with return value


def square(num):
    return num * num


result = square(4)
print("🔢 Square of 4 is:", result)

# ✅ 4. Default arguments


def describe(name, course="Python"):
    print(f"📘 {name} is enrolled in {course} course.")


describe("Moiz")
describe("Ali", "JavaScript")

# ✅ 5. *args → variable number of arguments


def add_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print("➕ Total Sum:", add_all(10, 20, 30))

# ✅ 6. **kwargs → keyword arguments


def show_info(**info):
    for key, value in info.items():
        print(f"{key} : {value}")


show_info(name="Moiz", age=20, course="AI")

# ✅ 7. Nested function


def outer():
    print("🔧 Outer function")

    def inner():
        print("⚙️ Inner function")

    inner()


outer()
