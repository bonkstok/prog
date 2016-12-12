import sqlite3
db = sqlite3.connect('sqlite3db.db')
cursor = db.cursor() # a cursor can iterate through the database.
cursor.execute("""
	CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, phone TEXT, 
						email TEXT unique, password TEXT)
				""")
db.commit()
db.close()#always close your database!