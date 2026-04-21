shirt=850
pants=1200
inners=300
discount_percentage=10
tax_percentage=18
total_cost=shirt+pants+inners
discount_percentage=total_cost*discount_percentage/100
after_discount=total_cost-discount_percentage
tax_percentage=after_discount*tax_percentage/100
final_cost=after_discount+tax_percentage

print("Total item cost:", total_cost)
print("Discount amount:", round(discount_percentage, 2))
print("After discount:", round(after_discount, 2))
print("Tax amount:", round(tax_percentage, 2))
print("Final bill amount:", round(final_cost, 2))