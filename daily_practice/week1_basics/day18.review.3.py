import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        grade TEXT
    )
''')

cursor.execute("INSERT INTO students VALUES (1, 'Dharun', 20, 'A')")
cursor.execute("INSERT INTO students VALUES (2, 'Rahul', 21, 'B')")
cursor.execute("INSERT INTO students VALUES (3, 'Priya', 19, 'A')")
conn.commit()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("All Students:")
for row in rows:
    print(row)
conn.close()