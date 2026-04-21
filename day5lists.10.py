# 3 items add பண்ணுவது
item1_name = "Shirt"
item1_price = 500

item2_name = "Pants"
item2_price = 800

item3_name = "Shoes"
item3_price = 1200

# Total calculate
total = item1_price + item2_price + item3_price
print("Total before removing item:", total)

# ஒரு item remove (example: Pants remove)
print("\nRemoving item:", item2_name)

total = total - item2_price

# New total
print("New total after removing item:", total)