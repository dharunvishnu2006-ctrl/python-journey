import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [3000, 4500, 4000, 5500, 6000]

plt.plot(months,sales)
plt.title('Monthly sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()