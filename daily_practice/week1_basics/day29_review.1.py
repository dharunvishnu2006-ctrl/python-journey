import pandas as pd

data = {
    'feature1': [10, 20, None, 40, 50],
    'feature2': [100, 200, 300, None, 500],
    'label': ['spam', 'ham', 'spam', 'ham', 'spam']
}

df = pd.DataFrame(data)

result = (
    df
    .dropna()                  
    .query("label == 'spam'")    
    .sort_values(by="feature1")  
)
print(result)