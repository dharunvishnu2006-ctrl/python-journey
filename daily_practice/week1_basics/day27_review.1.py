import time
import numpy as np

numbers = list(range(500000))

start = time.time()
result1 = [x * 3 for x in numbers]
end = time.time()
print(f"Loop: {end - start:.4f}s")

arr = np.array(numbers)
start = time.time()
result2 = arr * 3
end = time.time()
print(f"NumPy: {end - start:.4f}s")

print("Winner: NumPy! ")