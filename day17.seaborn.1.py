import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_theme(style='whitegrid')

data = {
    'name': ['Dharun', 'Rahul', 'Priya', 'Arun', 'Meena'],
    'age': [20, 25, 22, 28, 24],
    'bmi': [22.5, 27.3, 19.8, 30.1, 24.6],
    'bp': [120, 135, 110, 145, 125],
    'sugar': [90, 110, 85, 130, 95]
}
df = pd.DataFrame(data)

plt.figure(figsize=(8, 6))
sns.heatmap(df[['age','bmi','bp','sugar']].corr(), 
            annot=True, cmap='coolwarm')
plt.title('Health Metrics Correlation')
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(data=df[['bmi','bp','sugar']])
plt.title('Health Metrics Distribution')
plt.show()