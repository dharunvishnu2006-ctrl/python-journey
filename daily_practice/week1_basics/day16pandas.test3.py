import pandas as pd

customers = pd.DataFrame({
    'customer_id': [101, 102, 103],
    'name': ['Dharun', 'Rahul', 'Priya']
})

orders = pd.DataFrame({
    'customer_id': [101, 102, 104],
    'item': ['Biryani', 'Dosa', 'Idli'],
    'price': [250, 80, 60]
})
inner = pd.merge(customers, orders, on="customer_id", how="inner")
print("Inner:\n", inner)

left = pd.merge(customers, orders, on="customer_id", how="left")
print("\nLeft:\n", left)

outer_merge = pd.merge(customers, orders, on='customer_id', how='outer')
print("\nouter merge:\n",outer_merge)
