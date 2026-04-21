import csv

def read_students(filename: str) -> list:
    students = []
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append({
                    "name": row["name"],
                    "marks": int(row["marks"])
                })
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except ValueError:
        print("Error: Invalid marks data in CSV!")
    return students

def calculate_grade(marks: int) -> str:
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

def rank_students(students: list) -> list:
    sorted_students = sorted(students, key=lambda x: x["marks"], reverse=True)
    for index, student in enumerate(sorted_students):
        student["rank"] = index + 1
    return sorted_students

def display_results(students: list) -> None:
    ranked = rank_students(students)
    print("\n===== STUDENT GRADE TRACKER =====")
    for s in ranked:
        grade = calculate_grade(s["marks"])
        print(f"Rank {s['rank']}: {s['name']} | Marks: {s['marks']} | Grade: {grade}")
    print("==================================")
students = read_students("data/students.csv")
display_results(students)