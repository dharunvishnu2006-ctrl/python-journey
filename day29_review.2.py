import numpy as np

requests = np.array([100, 200, 1500, 300, 150, 2000,
                     400, 500, 1800, 200, 100, 300,
                     250, 400, 1600, 300, 200, 100,
                     500, 400, 300, 2500, 200, 100])

print(np.sum(requests))          
print(np.mean(requests))         
print(np.max(requests))         

suspicious = requests[requests > 1000]
print(suspicious)     

print(len(suspicious))