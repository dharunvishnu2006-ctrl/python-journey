import functools
import time

@functools.lru_cache(maxsize=128)
def check_ip_threat(ip_address):
    print(f"Checking database for {ip_address}...")
    time.sleep(2)  
    return f"{ip_address} — Threat Level: HIGH"

start = time.perf_counter()
print(check_ip_threat("192.168.1.1")) 
print(check_ip_threat("192.168.1.1"))  
print(check_ip_threat("10.0.0.1"))     
end = time.perf_counter()

print(f"\nTotal time: {end-start:.2f} seconds")
print(f"Cache info: {check_ip_threat.cache_info()}")

import functools
import time
def retry(max_attempts=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
            print("All attempts failed!")
            return None
        return wrapper
    return decorator

@retry(max_attempts=3, delay=1)
def fetch_model_data(model_id):
    import random
    if random.random() < 0.7: 
        raise Exception("API timeout!")
    return f"Model {model_id} data fetched!"

result = fetch_model_data("RandomForest")
print(result)