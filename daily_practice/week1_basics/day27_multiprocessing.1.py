import time
from concurrent.futures import ThreadPoolExecutor

hospitals = ["Apollo", "AIIMS", "Fortis", 
             "Manipal", "Max"]

def fetch_data(hospital):
    time.sleep(1)  
    return f"{hospital} data fetched!"

start = time.perf_counter()
for h in hospitals:
    fetch_data(h)
end = time.perf_counter()
print(f"Sequential: {end-start:.2f}s")

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=5) as ex:
    results = list(ex.map(fetch_data, hospitals))
end = time.perf_counter()
print(f"Parallel: {end-start:.2f}s")

for r in results:
    print(r)