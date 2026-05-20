import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'sales': [5000, 8000, 7000],
    'orders': [150, 200, 180]
}

df = pd.DataFrame(data)

sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation')
plt.show()