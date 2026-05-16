from contextlib import contextmanager

@contextmanager
def my_manager():
    print("Start!")
    yield
    print("End!")

with my_manager():
    print("Working!")