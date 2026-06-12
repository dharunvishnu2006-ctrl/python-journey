import time

def slow_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def fast_sum(numbers):
    return sum(numbers)

numbers = list(range(1000000))

start = time.perf_counter()
result1 = slow_sum(numbers)
end = time.perf_counter()
print(f"Slow sum: {result1} | Time: {end-start:.5f} seconds")

start = time.perf_counter()
result2 = fast_sum(numbers)
end = time.perf_counter()
print(f"Fast sum: {result2} | Time: {end-start:.5f} seconds")

import numpy as np

arr = np.array(numbers)

start = time.perf_counter()
result3 = np.sum(arr)
end = time.perf_counter()
print(f"NumPy sum: {result3} | Time: {end-start:.5f} seconds")