import asyncio
import time

async def download_dataset(name):
    print(f"Downloading {name}...")
    await asyncio.sleep(2)
    return f"{name} downloaded!"

async def main():
    start = time.perf_counter()
    results = await asyncio.gather(
        download_dataset("iris.csv"),
        download_dataset("mnist.csv"),
        download_dataset("titanic.csv"),
        download_dataset("housing.csv")
    )
    end = time.perf_counter()
    print(f"Total time: {end-start:.2f} seconds")
    for r in results:
        print(r)

asyncio.run(main())