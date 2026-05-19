import pandas as pd

week1 = pd.DataFrame({
    'day': ['Mon', 'Tue', 'Wed'],
    'orders': [150, 200, 180]
})

week2 = pd.DataFrame({
    'day': ['Thu', 'Fri', 'Sat'],
    'orders': [220, 300, 250]
})

result = pd.concat([week1,week2],ignore_index = True)
print(result)