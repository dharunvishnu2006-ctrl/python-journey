import asyncio
import time

async def fetch_server_log(server_id):
    print(f"Fetching log from Server {server_id}...")
    await asyncio.sleep(1)  
    print(f"Server {server_id} log received!")
    return f"Server {server_id} — No threats found!"

async def main():
    start = time.perf_counter()
 
    results = await asyncio.gather(
        fetch_server_log(1),
        fetch_server_log(2),
        fetch_server_log(3),
        fetch_server_log(4),
        fetch_server_log(5)
    )
    end = time.perf_counter()
    print(f"\nAll logs fetched in {end-start:.2f} seconds!")
    print(f"Results: {results}")

asyncio.run(main())

import threading 
import time

def parse_log(file_name):
    print(f"Parsing {file_name}...")
    time.sleep(1)  
    print(f"{file_name} parsed!")

start = time.perf_counter()

t1 = threading.Thread(target=parse_log, args=("server1.log",))
t2 = threading.Thread(target=parse_log, args=("server2.log",))
t3 = threading.Thread(target=parse_log, args=("server3.log",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end = time.perf_counter()
print(f"All logs parsed in {end-start:.2f} seconds!")

from concurrent.futures import ProcessPoolExecutor
import time

def train_model(model_name):
    print(f"Training {model_name}...")
    time.sleep(2) 
    return f"{model_name} — Accuracy: 95%!"

if __name__ == "__main__":
    models = ["RandomForest", "XGBoost", "NeuralNet"]
    
    start = time.perf_counter()
    
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(train_model, models))
    
    end = time.perf_counter()
    
    print(f"\nAll models trained in {end-start:.2f} seconds!")
    for r in results:
        print(r)