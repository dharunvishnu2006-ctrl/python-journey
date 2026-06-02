import pandas as pd

data = {
    'city': ['Chennai', 'Mumbai', 'Chennai', 'Delhi', 'Mumbai'],
    'sales': [5000, 8000, 3000, 7000, 6000]
}

df = pd.DataFrame(data)
result = df.groupby('city')['sales'].sum()
print(result)