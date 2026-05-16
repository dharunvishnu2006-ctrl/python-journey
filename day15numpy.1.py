import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a + 10)
print(a * 2)
print(a ** 2)

x = np.array([10, 20, 30])
y = np.array([1, 2, 3])
print(x + y)
print(x * y)

bp = np.array([120, 145, 118, 160, 135])
print("Mean:", np.mean(bp))
print("Std:", np.std(bp))
print("Normal:", bp < 140)