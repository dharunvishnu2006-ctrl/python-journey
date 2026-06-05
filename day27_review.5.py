import asyncio
import time

async def fetch(name):
    await asyncio.sleep(1)
    return f"{name} fetched!"

async def sequential():
    start = time.perf_counter()
    r1 = await fetch("Dharun")
    r2 = await fetch("Amma")
    r3 = await fetch("Appa")
    end = time.perf_counter()
    print(f"Sequential: {end-start:.2f}s")

async def parallel():
    start = time.perf_counter()
    results = await asyncio.gather(
        fetch("Dharun"),
        fetch("Amma"),
        fetch("Appa")
    )
    end = time.perf_counter()
    print(f"Parallel: {end-start:.2f}s")

async def main():
    await sequential()
    await parallel()

asyncio.run(main())