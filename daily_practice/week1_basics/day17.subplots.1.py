import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

days = [1, 2, 3, 4, 5, 6, 7]
orders = [150, 200, 180, 220, 300, 250, 280]
axes[0][0].plot(days, orders, color='blue')
axes[0][0].set_title('Zomato Daily Orders')
axes[0][0].set_xlabel('Day')
axes[0][0].set_ylabel('Orders')

cities = ['Chennai', 'Mumbai', 'Delhi', 'Bangalore']
revenue = [5000, 8000, 7000, 9000]
axes[0][1].bar(cities, revenue, color='green')
axes[0][1].set_title('City Revenue')

matches = [1, 2, 3, 4, 5]
scores = [180, 165, 200, 175, 190]
axes[1][0].plot(matches, scores, color='orange')
axes[1][0].set_title('IPL Scores')

products = ['Biryani', 'Dosa', 'Idli', 'Parotta']
sales = [500, 300, 200, 400]
axes[1][1].bar(products, sales, color='red')
axes[1][1].set_title('Food Sales')

fig.tight_layout()
plt.show()