import numpy as np
import pandas as pd

request_counts = np.array([1500, 200, 800, 300, 100, 2000, 150])

print("Array:", request_counts)
print("Shape:", request_counts.shape)
print("Mean requests:", np.mean(request_counts))
print("Max requests:", np.max(request_counts))
print("Suspicious (>1000):", request_counts[request_counts > 1000])