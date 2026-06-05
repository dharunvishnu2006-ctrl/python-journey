import time
import numpy as np

numbers = list(range(1000000))
arr = np.array(numbers)

start = time.perf_counter()
total1 = sum(numbers)
end = time.perf_counter()
loop_time = end - start
print(f"Loop: {loop_time:.4f}s")

start = time.perf_counter()
total2 = np.sum(arr)
end = time.perf_counter()
numpy_time = end - start
print(f"NumPy: {numpy_time:.4f}s")

faster = round(loop_time / numpy_time)
print(f"NumPy is {faster}x faster!")