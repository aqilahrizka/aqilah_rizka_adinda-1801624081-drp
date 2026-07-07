import sqlite3

conn = sqlite3.connect("affirmation.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM afirmasi")

data = cursor.fetchall()

for item in data:
    print(item)

conn.close()
