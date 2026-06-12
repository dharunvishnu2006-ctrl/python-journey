units = 250

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100*5 + (units-100)*8
elif units <= 500:
    bill = 100*5 + 100*8 + (units-200)*10
else:
    bill = 100*5 + 100*8 + 300*10 + (units-500)*12

print(f'Bill: ₹{bill}')