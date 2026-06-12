import pandas as pd

data = {
    'city': ['Chennai', 'Mumbai','Chennai', 'Delhi', 'Mumbai'],
    'sales': [5000, 8000, 3000, 7000, 6000]
}
df = pd.DataFrame(data)

print(df.groupby('city')['sales'].agg(['sum', 'mean', 'max']))
