import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'revenue': [5000, 7000, 6000, 8000, 9000],
    'customers': [100, 140, 120, 160, 180]
}
df = pd.DataFrame(data)
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data
data = {
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'revenue': [5000, 7000, 6000, 8000, 9000],
    'customers': [100, 140, 120, 160, 180]
}

df = pd.DataFrame(data)
fig, axes = plt.subplots(2, 1, figsize=(8, 8))

axes[0].plot(df['month'], df['revenue'],color = 'blue')
axes[0].set_title('Revenue Trend')
axes[0].set_xlabel('Month')
axes[0].set_ylabel('Revenue')

corr = df[['revenue', 'customers']].corr()

sns.heatmap(corr, annot=True, cmap='coolwarm', ax=axes[1])

axes[1].set_title('Revenue vs Customers')

fig.tight_layout()
plt.show()