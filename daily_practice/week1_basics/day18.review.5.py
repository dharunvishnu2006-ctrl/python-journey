import sqlite3
import plotly.express as px
import pandas as pd

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute("SELECT name, age FROM students")
rows = cursor.fetchall()
conn.close()

df = pd.DataFrame(rows, columns=['name', 'age'])

fig = px.bar(df, x='name', y='age',
             title='Student Ages',
             color='name')
fig.write_html('students_chart.html')
fig.show()