students = {
    "dharun": 95,
    "ram": 88,
    "kumar":76,
    "priya": 92
}
topper = max(students, key=students.get)
print("Topper:", topper, "-", students[topper])

average = sum(students.values()) / len(students)
print("Average Marks:", round(average, 2))

print("\nPass / Fail Status:")
for name, marks in students.items():
    if marks >= 80:
        print(name, ":", "Pass")
    else:
        print(name, ":", "Fail")
