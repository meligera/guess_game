import sqlite3

connection = sqlite3.connect('db')
cursor = connection.cursor()
cursor.execute('SELECT * FROM level_1')
print(cursor.fetchall())

connection.commit()
cursor.close()
connection.close()