def add_all(*args):
    total = 0
    for num in args:
        total = total+num
    return total

print(add_all(1,2,3))
print(add_all(10,20,30,40))
print(add_all(5,10))