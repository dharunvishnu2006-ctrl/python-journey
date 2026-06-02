import numpy as np

marks = np.array([78, 45, 92, 38, 85])

result = np.where(marks >= 50, 'Pass', 'Fail')

print("Marks :", marks)
print("Result :", result)

average = np.mean(marks)
print("Class Average :", average)