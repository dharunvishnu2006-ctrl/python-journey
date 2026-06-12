import pandas as pd

data = {
    "name": ["Ravi", "Priya", "Kumar", "Meena", "Raja"],
    "marks": [78, 92, 65, 88, 71]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

high_marks = df[df["marks"] > 80]

print("\nStudents with marks > 80:")
print(high_marks)
