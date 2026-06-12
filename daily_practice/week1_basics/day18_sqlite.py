import sqlite3

conn = sqlite3.connect('aarogya.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        disease TEXT,
        city TEXT
    )
''')

cursor.execute("INSERT INTO patients VALUES (1, 'Dharun', 20, 'Fever', 'Chennai')")
cursor.execute("INSERT INTO patients VALUES (2, 'Rahul', 25, 'Diabetes', 'Mumbai')")
cursor.execute("INSERT INTO patients VALUES (3, 'Priya', 22, 'BP', 'Delhi')")
conn.commit()

cursor.execute("SELECT * FROM patients")
rows = cursor.fetchall()
print("All Patients:")
for row in rows:
    print(row)

conn.close()