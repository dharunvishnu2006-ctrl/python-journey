import functools
import time
import random

def retry(max_attempts=4, delay=1):
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

@retry(max_attempts=4, delay=1)
def train_model(name):
    if random.random() < 0.6: 
        raise Exception("GPU out of memory!")
    return f"{name} trained successfully!"

print(train_model("XGBoost"))