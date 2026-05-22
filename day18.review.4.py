import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM students WHERE grade='A'")
rows = cursor.fetchall()
print("Grade A Students:")
for row in rows:
    print(row)

cursor.execute("SELECT * FROM students WHERE age>19")
rows = cursor.fetchall()
print("\nAge > 19 Students:")
for row in rows:
    print(row)

conn.close()