def calculate_bill(shirt,pant,shoes,discount,tax):
    total = shirt + pant + shoes
    discounted_amount = total * (discount / 100)
    discounted_total = total - discounted_amount
    tax_amount = discounted_total * (tax / 100)
    final_bill = discounted_total + tax_amount
    return final_bill
print(calculate_bill(500,800,1200, 10, 18))