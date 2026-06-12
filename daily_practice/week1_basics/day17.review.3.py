import matplotlib.pyplot as plt
fig, axes = plt.subplots(2, 1, figsize=(10, 8))

weeks = [1, 2, 3, 4]
transactions = [5000, 7000, 6500, 8000]
axes[0].plot(weeks, transactions, color='blue')
axes[0].set_title('UPI transactions')
axes[0].set_xlabel('weeks')
axes[0].set_ylabel('transactions')

cities = ['Chennai', 'Mumbai', 'Delhi']
users = [10000, 15000, 12000]
axes[1].bar(cities, users, color='green')
axes[1].set_title('City users')

fig.tight_layout()
plt.show()