import matplotlib.pyplot as plt

products = ['Biryani', 'Dosa', 'Idli', 'Parotta', 'Chapati']
revenue = [5000, 3000, 2000, 4000, 2500]

plt.bar(products,revenue,color='orange')
plt.title('Food Revenue')
plt.xlabel('Products')
plt.ylabel('Revenue')
plt.show()