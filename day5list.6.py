cart = []
cart.append(("Rice", 50))
cart.append(("Dal", 80))
cart.append(("Oil", 150))
cart.append(("Sugar", 45))

print("your cart:")
total = 0
for item, price in cart:
    print(f"  {item}: Rs.{price}")
    total += price

print(f"Total: Rs.{total}")

# Remove one item
cart.remove(("Dal", 80))
print("\nAfter removing Dal:")
total = sum(price for item, price in cart)
print(f"New Total: Rs.{total}")