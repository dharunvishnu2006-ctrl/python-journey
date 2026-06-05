import asyncio
import time

async def fetch(name):
    await asyncio.sleep(1)
    return f"{name} fetched!"

async def main():
    start = time.perf_counter()
    
    results = await asyncio.gather(
        fetch("Dharun"),
        fetch("Amma"),
        fetch("Appa")
    )
    
    end = time.perf_counter()
    print(f"Time: {end-start:.2f}s")
    for r in results:
        print(r)

asyncio.run(main())