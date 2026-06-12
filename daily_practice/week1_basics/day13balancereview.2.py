def fibonacci(n):
    a, b = 0, 1
    for n in range(n):
        yield a
        a, b = b, a + b
gen = fibonacci(6)

for num in gen:
    print(num)
