import asyncio
import time

async def fetch_report(hospital):
    await asyncio.sleep(1)
    return f"{hospital} report ready!"

async def main():
    start = time.perf_counter()

    results = await asyncio.gather(
        fetch_report("Apollo"),
        fetch_report("AIIMS"),
        fetch_report("Fortis"),
        fetch_report("Max")
    )

    end = time.perf_counter()
    print(f"Time: {end-start:.2f}s")
    for r in results:
        print(r)

asyncio.run(main())