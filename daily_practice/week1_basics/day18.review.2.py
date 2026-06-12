import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'city': ['Chennai', 'Mumbai', 'Delhi', 'Bangalore', 'Hyderabad'],
    'patients': [500, 800, 700, 900, 600]
})

fig = px.bar( df,x='city',y='patients',color='city', title='AAROGYA — City wise Patients')

fig.write_html('patients.html')
fig.show()