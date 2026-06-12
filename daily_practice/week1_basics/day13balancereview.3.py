import functools

def your_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Function Starting!")
        func(*args, **kwargs)
        print("Function Done!")
    return wrapper


@your_decorator
def greet(name):
    print(f"Hello {name}!")

greet("Dharun")