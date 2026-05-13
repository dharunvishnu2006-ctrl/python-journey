import functools

def shout(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print("=== START ===")
        result = func(*args,**kwargs)
        print("=== END ===")
        return result
    return wrapper

@shout
def greet(name):
    print(f"Hello {name}!")

greet("Dharun")

import time
def timer(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print(f"Time: {time.time()-start:.4f}s")
        return result
    return wrapper
@timer
def calculate(n):
    return sum(range(n))
print(calculate(1000000))