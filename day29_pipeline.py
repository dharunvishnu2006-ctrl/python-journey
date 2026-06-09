import pandas as pd

data = {
    'ip_address': ['192.168.1.1', '10.0.0.1', None, '192.168.1.1', '172.16.0.1'],
    'status': ['suspicious', 'normal', 'suspicious', 'suspicious', 'normal'],
    'requests': [1500, 200, 800, 300, 100],
    'timestamp': ['2025-01-01', '2025-01-01', '2025-01-01', '2025-01-02', '2025-01-02']
}

df = pd.DataFrame(data)
print(df)
clean_df = (df
            .dropna()
            .query("status == 'suspicious' ")
            .sort_values('requests', ascending=False)
            )

print(clean_df)