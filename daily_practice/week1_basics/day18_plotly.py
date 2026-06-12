import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'orders': [150, 200, 180, 220, 300]
})

fig = px.line(df, x='day', y='orders',
              title='Zomato Weekly Orders')
fig.write_html('zomato_chart.html')
fig.show()

df2 = pd.DataFrame({
    'city': ['Chennai', 'Mumbai', 'Delhi', 'Bangalore'],
    'revenue': [5000, 8000, 7000, 9000]
})

fig2 = px.bar(df2, x='city', y='revenue',
              title='City wise Revenue',
              color='city')
fig2.write_html('city_revenue.html')
fig2.show()