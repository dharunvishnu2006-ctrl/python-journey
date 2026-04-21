import json
import os

FILE_NAME = "students.json"
def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    data = load_data()
    data.append({"name": name, "marks": marks})
    save_data(data)

    print("Student added successfully!")

def view_students():
    data = load_data()

    if not data:
        print("No students found.")
        return

    print("\n--- Student List ---")
    for i, student in enumerate(data, start=1):
        print(f"{i}. {student['name']} - {student['marks']}")


def update_marks():
    name = input("Enter student name to update: ")
    data = load_data()

    for student in data:
        if student["name"].lower() == name.lower():
            new_marks = int(input("Enter new marks: "))
            student["marks"] = new_marks
            save_data(data)
            print("Marks updated!")
            return

    print("Student not found.")

def delete_student():
    name = input("Enter student name to delete: ")
    data = load_data()
    new_data = [s for s in data if s["name"].lower() != name.lower()]

    if len(new_data) == len(data):
        print(" Student not found.")
    else:
        save_data(new_data)
        print("Student deleted!")
while True:
    print("\n--- MENU ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_marks()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print(" Invalid choice")