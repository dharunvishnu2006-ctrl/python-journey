import time
from concurrent.futures import ThreadPoolExecutor

patients = ["Dharun", "Amma", "Appa",
            "Ravi", "Priya"]

def process_patient(name):
    time.sleep(1)
    return f"{name} processed!"

start = time.perf_counter()

with ThreadPoolExecutor(max_workers=5) as ex:
    results = list(ex.map(process_patient, patients))

end = time.perf_counter()
print(f"Time: {end-start:.2f}s")

for r in results:
    print(r)