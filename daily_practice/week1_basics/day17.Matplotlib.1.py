import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
orders = [150, 200, 180, 220, 300, 250, 280]

plt.plot(days, orders)
plt.title('Zomato Daily Orders')
plt.xlabel('Day')
plt.ylabel('Orders')
plt.show()

cities = ['Chennai', 'Mumbai', 'Delhi', 'Bangalore']
revenue = [5000, 8000, 7000, 9000]

plt.bar(cities, revenue)
plt.title('City wise Revenue')
plt.xlabel('City')
plt.ylabel('Revenue')
plt.show()