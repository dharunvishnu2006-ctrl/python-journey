import numpy as np

arr = np.arange(1, 11)
even_numbers = arr[arr % 2 == 0]

print("Original Array:", arr)
print("Even Numbers:", even_numbers)