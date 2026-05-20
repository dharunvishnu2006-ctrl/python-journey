import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'city': ['Chennai', 'Mumbai', 'Delhi', 'Chennai', 'Mumbai'],
    'sales': [5000, 8000, 7000, 6000, 9000],
    'orders': [150, 200, 180, 160, 220]
}
df = pd.DataFrame(data)
df = pd.DataFrame(data)

plt.figure(figsize=(8, 6))
sns.heatmap(df[['sales','orders']].corr(), 
            annot=True, cmap='coolwarm')
plt.title('Sales vs Orders correlation')
plt.show()
