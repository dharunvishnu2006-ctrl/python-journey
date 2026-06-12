import asyncio
import time

async def fetch_patient(name):
    await asyncio.sleep(1)
    return f"{name} data fetched!"

async def main():
    start = time.perf_counter()
    
    results = await asyncio.gather(
        fetch_patient("Dharun"),
        fetch_patient("Amma"),
        fetch_patient("Appa"),
        fetch_patient("Ravi"),
        fetch_patient("Priya")
    )
    
    end = time.perf_counter()
    print(f"Time: {end-start:.2f}s")
    
    for r in results:
        print(r)

asyncio.run(main())