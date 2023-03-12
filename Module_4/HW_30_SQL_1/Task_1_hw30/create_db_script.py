import sqlite3

connection = sqlite3.connect('hw30_sqlite_db')

cursor = connection.cursor()

connection.commit()
connection.close()