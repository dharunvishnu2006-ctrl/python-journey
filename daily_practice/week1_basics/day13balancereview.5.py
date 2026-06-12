from contextlib import contextmanager

@contextmanager
def file_manager(filename):
    f = open(filename, "w")
    try:
        yield f 
    finally:
        f.close() 

with file_manager("test.txt") as f:
    f.write("Hello from Dharun!")
with open("test.txt", "r") as f:
    print(f.read())