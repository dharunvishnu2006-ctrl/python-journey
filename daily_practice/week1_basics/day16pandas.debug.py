import pandas as pd

students = pd.DataFrame({
    'student_id': [1, 2, 3],
    'name': ['Dharun', 'Rahul', 'Priya']
})

marks = pd.DataFrame({
    'student_id': [1, 2, 3],
    'math': [95, 80, 70]
})

result = pd.merge(students, marks, on='student_id', how='inner')
print(result)