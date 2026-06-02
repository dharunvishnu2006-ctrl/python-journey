import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'day': ['Mon', 'Tue', 'Wed'],
    'orders': [100, 200, 150]
})

fig = px.line(df, x='day', y='orders',
              title='Daily Orders')
fig.write_html('orders.html')
fig.show()