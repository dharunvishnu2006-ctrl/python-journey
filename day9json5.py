import json

students = {
    "student1": {
        "name": "Dharun",
        "marks": {
            "python": 95,
            "maths": 88,
            "english": 76
        }
    },
    "student2": {
        "name": "Ram",
        "marks": {
            "python": 82,
            "maths": 90,
            "english": 85
        }
    }
}

print(students["student1"]["name"])
print(students["student1"]["marks"]["python"])
print(students["student2"]["marks"]["maths"])

with open("students.json", "w") as f:
    json.dump(students, f, indent=2)

print("Saved!")