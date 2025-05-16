import sqlite3

conn=sqlite3.connect('test.db')
cur=conn.cursor()

data=cur.execute('''Select * from STUDENT''')
print(data)
for row in data:
    print(row)