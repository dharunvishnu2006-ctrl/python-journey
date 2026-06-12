import pandas as pd

students = pd.DataFrame({
    'student_id': [1, 2, 3, 4],
    'name': ['Dharun', 'Rahul', 'Priya', 'Arun']
})

marks = pd.DataFrame({
    'student_id': [1, 2, 3],
    'math': [95, 80, 70],
    'science': [88, 75, 90]
})

left = pd.merge(students,marks, on="student_id", how="left")
print("\nleft:\n", left)

avg_math = left['math'].mean()
print("\nAverage Math Marks:", avg_math)