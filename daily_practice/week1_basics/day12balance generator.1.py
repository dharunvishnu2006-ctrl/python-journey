def countdown(n):
    while n > 0:
        yield n 
        n -= 1

for num in countdown(5):
    print(num)    

squares = (x**2 for x in range(1,6))     
for s in squares:
    print (s)   