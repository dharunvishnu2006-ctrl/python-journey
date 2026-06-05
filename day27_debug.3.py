import time
from concurrent.futures import ThreadPoolExecutor

patients = ["Dharun", "Amma", "Appa"]

def process(name):
    time.sleep(1)
    return f"{name} done!"

start = time.perf_counter()

with ThreadPoolExecutor(max_workers=3) as ex:
    results = list(ex.map(process, patients))

end = time.perf_counter()
print(f"Time: {end-start:.2f}s")
for r in results:
    print(r)