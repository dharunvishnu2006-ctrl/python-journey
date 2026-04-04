cart = []
cart.append(("Dhal",50))
cart.append(("sugar",120))
cart.append(("soap",90))
print("your cart:")
total = 0
for item, price in cart:
   print(f"{item}: rs.{price}")
   total += price

cart.remove(("Dhal",50))
print ("After removing Dhal:")
total =sum (price for item,price in cart)
print(f"New total:rs.{total}")