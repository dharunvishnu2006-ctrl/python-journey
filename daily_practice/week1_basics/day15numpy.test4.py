import numpy as np

bp_readings = np.array([
    [120, 125, 118],  
    [145, 150, 148],  
    [135, 130, 132]   
])

avg = np.mean(bp_readings, axis=1)
print("Avg BP:", avg)

print("Max BP:", np.max(bp_readings))