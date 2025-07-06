import csv


# 1. Create a CSV file and write data to it
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City", "Contact"])
    writer.writerow(["Abdul Moiz", 20, "Lahore", "0326-0107654"])
    writer.writerow(["Ali", 22, "Karachi", "0333-1234567"])
    writer.writerow(["Sara", 19, "Islamabad", "0344-9876543"])
    writer.writerow(["Ahmed", 21, "Peshawar", "0355-4567890"])
    print("✅ CSV file created and data written successfully.")

# 2. Read the entire CSV file
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    print("\n📄 CSV File Content: ")
    for row in reader:
        print(row)

# 3. append data to the CSV file
with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Fatima", 23, "Quetta", "0366-6543210"])
    print("\n📝 Data appended to CSV file successfully.")

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    print("\n📄 Updated CSV File Content: ")
    for row in reader:
        print(row)
