import time
import numpy as np

numbers = list(range(100000))
arr = np.array(numbers)

start = time.perf_counter()
result = arr * 2
end = time.perf_counter()

print(f"Time: {end - start:.6f}s")