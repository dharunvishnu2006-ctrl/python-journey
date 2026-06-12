import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'sales': [3000, 4500, 4000, 5500, 6000]
})

fig = px.line(df, x='month',y='sales',title='Monthly Sales Trend',markers=True)
fig.write_html('sales_trend.html')
fig.show()