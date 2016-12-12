import sqlite3
import os.path

def connectToDatabase():
	database = "sqlite3db.db"
	if os.path.isfile(database):
		print("Database already exists. Not creating a new one.")
		db = sqlite3.connect(database)
		cursor = db.cursor()	
	else:
		db = sqlite3.connect(database)
		cursor = db.cursor()
	return (db, cursor)

def closeDatabase(db):
	db.close()

def deleteUsers(cursor,db):
	cursor.execute("SELECT id, name FROM users")
	db.commit()
	result = cursor.fetchall() #get the results in array
	for row in result:
		print("{}\t{}".format(row[0],row[1])) # 0 is first item in the query above. In this case itś the id.
	print("Please enter the ID that you would like to delete.")
	id_delete = input(">>")	
	cursor.execute("DELETE FROM users WHERE id =  ?",(id_delete,))
	print("Deleting row with ID:{}".format(id_delete))
	cont = True
	while cont:
		c = input("Enter Y or y to enter another user: ")
		if c is 'Y' or c is "y":
			print("Please enter the ID that you would like to delete.")
			id_delete = input(">>")	
			cursor.execute("DELETE FROM users WHERE id =  ?",(id_delete,))
			print("Deleting row with ID:{}".format(id_delete))
		else:
			cont = False


def displayInfo(cursor,db):
	print("Enter the information(id, name, phone, email and password) you would like to display below seperated by a comma!:")
	info= input(">>")
	info_request = info.split(',')
	i = 0
	#print(info_request)
	#print(info_request[0])
	if len(info_request) == 5:
		cursor.execute("SELECT * FROM users")
		db.commit()
		result = cursor.fetchall()
		print("{}\t{}\t\t\t{}\t\t{}\t\t\t\t{}".format(info_request[0],info_request[1],info_request[2],info_request[3],info_request[4]))
		for row in result:
			print("{}\t{}\t\t\t{}\t\t{}\t\t\t\t{}".format(row[0],row[1],row[2],row[3], row[4]))
	elif len(info_request) != 5:
		print("Please enter five keywords. Queries with less or more keywords are being developed.")
	



			# while i < len(info_request):
			# print(info_request[i])
			# for row in result:
			# 	print("{}, {},{}. {}".format(row[0],row[1],row[2],row[3]))
			# 	i = i + 1

def findInfo(cursor):
	pass



def printOptions():
	print("\nSelect one of our functions listed below!")
	print("1. Add user to the database.")
	print("2. Add multiple users to the database.")
	print("3. Delete user from the database.")
	print("4. Display information.")
	print("Create a table")
	try:
		keuze = int(input(">>> "))
		return keuze
	except ValueError:
		"Please use numbers![1:6] and no letters!"

def addMultipleUsers(cursor):
	users = input("How many users would you like to add? ")
	i = 0
	while i < int(users):
		email = input("Please enter your email>>")
		cursor.execute("SELECT email from users WHERE email = ?", (email,))
		usedemail = cursor.fetchall() #get one result
		if len(usedemail) > 0:	
		#print(len(usedemail))
			print("The e-mail address {} has already been used, please use another e-mail address".format(email))
			email = input("Please enter your e-mail address again>>")
		else:
			pass
		naam = input("Please enter your name>>")
		phone = input("Please enter your phonenumber>>")
		password=input("Please enter your password>>")
		add = [(naam, phone, email, password)]
		cursor.executemany("""INSERT INTO USERS(name, phone,email,password)
					VALUES(?,?,?,?)""",(add))
		i = i + 1
	

def addUser(cursor):
	email = input("Please enter your email>>")
	cursor.execute("SELECT email from users WHERE email = ?", (email,))
	usedemail = cursor.fetchall() #get one result
	if len(usedemail) > 0:	
		#print(len(usedemail))
		print("The e-mail address {} has already been used, please use another e-mail address".format(email))
	else:
		pass
	
	naam = input("Please enter your name>>")
	phone = input("Please enter your phonenumber>>")
	password=input("Please enter your password>>")
	add = [(naam, phone, email, password)]
	print("Adding information to the database.")
	cursor.executemany("""INSERT INTO USERS(name, phone,email,password)
					VALUES(?,?,?,?)""",(add))


def main():
	# db = sqlite3.connect('sqlite3db.db')
	# cursor = db.cursor() # a cursor can iterate through the database.
	db, cursor = connectToDatabase() # create the database connection anda cursor @ functions above.
	#cursor = datacon(1)
	#db = datacon[0]
	cursor.execute("""
		CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, phone TEXT, 
	 						email TEXT unique, password TEXT)
					""")
	db.commit()
	
	while(True):
		keuze = int(printOptions())
		if keuze == 1:
			addUser(cursor)
			db.commit()
			continue
		if keuze == 2:
			addMultipleUsers(cursor)
			db.commit()
			continue
		if keuze == 3:
			deleteUsers(cursor,db)
			db.commit()
			continue
		if keuze == 4:
			displayInfo(cursor,db)
			continue
		else:
			print("Updates with more functions will come shortly.")
			break
	# name1 = "
	
	
	
	"
	# phone1 = "334453"
	# email1 = ""
	# password1 = input("{} please enter your password:".format(name1))

	# name2 = "Henk"
	# phone2 = "334453"
	# email2 = "@.com"
	# password2 = input("{} please enter your password:".format(name2))
	# try:
	# 	cursor.execute("""INSERT INTO USERS(name, phone,email,password)
	# 						VALUES(?,?,?,?)
	# 					""", (name1,phone1,email1,password1))
	# 	print("First user inserted.")

	# 	cursor.execute("""INSERT INTO USERS(name, phone,email,password)
	# 						VALUES(?,?,?,?)
	# 					""", (name2,phone2,email2,password2))
	# 	print("Second user inserted.")
	# except sqlite3.IntegrityError:
	# 	print("Error: The e-mail has to be unique.")
	#db.commit()
	closeDatabase(db)#always close your database!  
if __name__ == '__main__':
	main()
