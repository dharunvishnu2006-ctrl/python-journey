import time
import numpy as np

patients = list(range(1000000))

start = time.perf_counter()
result1 = [x * 2 for x in patients]
end = time.perf_counter()
print(f"Loop time: {end-start:.4f} seconds")

arr = np.array(patients)
start = time.perf_counter()
result2 = arr * 2
end = time.perf_counter()
print(f"NumPy time: {end-start:.4f} seconds")