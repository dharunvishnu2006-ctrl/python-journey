import numpy as np

a = np.array([10, 20, 30, 40, 50])
print(a[0])
print(a[-1])
print(a[1:4])
print(a[::2])

print(a[a > 25])

bp = np.array([120, 145, 118, 160, 135])
status = np.where(bp > 140, "High Risk", "Normal")
print(status)

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix[1, 2])
print(matrix[:, 1])