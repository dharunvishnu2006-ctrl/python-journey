import pandas as pd
students = pd.DataFrame({
    "student_id": [1, 2, 3, 4],
    "name": ["Ravi", "Priya", "Kumar", "Meena"]
})

marks = pd.DataFrame({
    "student_id": [1, 2, 3, 5],
    "marks": [85, 92, 78, 88]
})

inner = pd.merge(students, marks, on="student_id", how="inner")
print("Inner:\n", inner)

left = pd.merge(students, marks, on="student_id", how="left")
print("\nLeft:\n", left)

df1 = pd.DataFrame({"name": ["Ravi"], "marks": [85]})
df2 = pd.DataFrame({"name": ["Priya"], "marks": [92]})
combined = pd.concat([df1, df2], ignore_index=True)
print("\nConcatenated:\n", combined)