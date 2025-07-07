import json


def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file)


def load_data():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        students = []


students = []


def show_menu():
    print("\n----- Student Management System -----")
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Search Student (by Roll Number)")
    print("4. Update Student Details")
    print("5. Delete Student")
    print("6. Exit")

# Add Student


def add_student():
    name = str(input("Enter the student Name: "))
    roll = int(input("Enter the roll number: "))
    clas = str(input("Enter the class: "))
    marks = int(input("Enter the Marks: "))
    student = {
        "name": name,
        "roll": roll,
        "class": clas,
        "marks": marks
    }

    students.append(student)
    save_data()
    print("Student added Successfully.")

# Student List


def list_student():
    if not students:
        print("No student Found!")
        return
    for s in students:
        print(
            f"Name: {s['name']}, Rollno: {s['roll']} ,Class: {s['class']}, Marks: {s['marks']}")

# Search Student


def search_student():
    roll = int(input("Enter roll number to search: "))
    for s in students:
        if s['roll'] == roll:
            print(
                f"Name: {s['name']}, Class : {s['class']}, Marks: {s['marks']} ")
            return
    print("Student not Found.")
# Update Student


def update_student():
    roll = int(input("Enter roll number to update: "))
    for s in students:
        if s['roll'] == roll:
            s['name'] = input("Enter new name: ")
            s['class'] = input("Enter new class: ")
            s['marks'] = int(input("Enter new marks: "))
            save_data()
            print("✅ Student data updated successfully!")
            return
    print("❌ Student not found.")

# Delete Student


def delete_student():
    roll = int(input("Enter roll number to delete: "))
    for s in students:
        if s['roll'] == roll:
            students.remove(s)
            save_data()
            print("✅ Student deleted successfully!")
            return
    print("❌ Student not found.")


load_data()
while True:
    show_menu()
    choice = int(input("Select an option (1-6): "))
    if choice == 1:
        add_student()
    elif choice == 2:
        list_student()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_student()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        print("Thank you! Exiting program")
        break
    else:
        print("Invalid option! Please try again.")
