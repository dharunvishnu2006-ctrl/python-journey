students = {
    "Arun": 78,
    "Bala": 45,
    "Charan": 92,
    "Deepak": 60,
    "Ezhil": 50
}
topper = max(students, key=students.get)
print("Topper:", topper, "-", students[topper])

average = sum(students.values()) / len(students)
print("Average Marks:", round(average, 2))

print("\nPass / Fail Status:")
for name, marks in students.items():
    if marks >= 50:
        print(name, ":", "Pass")
    else:
        print(name, ":", "Fail")
