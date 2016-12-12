#
import sqlite3
import os.path
from tabulate import tabulate
#import sys for exit
def connectToDatabase():
	database = "license_test.db"
	if os.path.isfile(database):
		print("Database already exists. Not creating a new one.")
		db = sqlite3.connect(database)
		cursor = db.cursor()
	else:
		db = sqlite3.connect(database)
		cursor = db.cursor()
		publisher_ini = "CREATE TABLE IF NOT EXISTS publisher(publisher_name TEXT PRIMARY KEY , contactpersoon TEXT)"
		license_ini ="CREATE TABLE IF NOT EXISTS license(license_code TEXT NOT NULL, license_name TEXT NOT NULL, license_cat TEXT NOT NULL,license_comment TEXT, publisher_name TEXT NOT NULL, FOREIGN KEY(publisher_name) REFERENCES publisher(publisher_name), PRIMARY KEY(license_code, publisher_name))"
		cursor.execute(publisher_ini)
		db.commit()
		cursor.execute(license_ini)
		db.commit() 	
	return (db, cursor)


def executeQuery(cursor,query):
	cursor.execute(query) #do we really need this as a function?
	return cursor.fetchall()


def checkStringNotEmpty(text_input):
	while(True):
		to_return = input(text_input)
		if not to_return:
			continue 
		else:
			return to_return
			break


def printMenu():
	print("1. Add license.")
	print("2. Add publisher.")
	print("3. Search license.")
	print("4. Delete publisher or license.")
	print("5. Export license to csv.")
	print("6. Quit.")
	try:
		keuze = int(input(">>>"))
		return keuze
	except ValueError:
		print("Please enter a number![1:6].")

def printLicense(db,cursor):
	result = executeQuery(cursor,"SELECT * FROM license")
	print(tabulate(result, headers=["License code", "Name", "Category", "Comments", "Publisher"]))
def searchLicense(db,cursor):
	search = input("Search:")

	cursor.execute("SELECT * from license WHERE publisher_name LIKE ? or license_cat LIKE ?",('%'+search+'%','%'+search+'%'))#the % are wildcards. 
	result = cursor.fetchall()
	print(tabulate(result, headers=["License code", "Name", "Category", "Comments", "Publisher"]))#tabulate is a package that outputs a nice format list.

def addPublisher(db, cursor):
	name_pub = checkStringNotEmpty("Please enter the name of the publisher:") #Cannot be null
	contactpersoon_pub = checkStringNotEmpty("Please enter the name of the contactperson:") #Can be null, preferable not.  

	add = [(name_pub, contactpersoon_pub)]
	print(add)
	try:
		cursor.execute("""INSERT INTO publisher(publisher_name, contactpersoon)
					VALUES(?,?)""",(name_pub, contactpersoon_pub))
		db.commit()
	except sqlite3.IntegrityError as e:
		print(e)
		print('Publisher {} already exists. Did not write to database.'.format(name_pub))
		db.rollback()
def addLicense(db,cursor):
	license_code = checkStringNotEmpty("Enter the license code:")
	license_name = checkStringNotEmpty("Enter the software-package name:")
	license_cat  = checkStringNotEmpty("Enter license category:") #Still not sure whether or not cat can NULL or not.
	comments = input("Comments:") #This can be null, hence why function checkString is not called.
	publisher_enter = input("Please one of the publishers displayed above:")
	try:
		cursor.execute("INSERT INTO license VALUES(?,?,?,?,?)",(license_code,license_name, license_cat, comments, publisher_enter))
		db.commit()
	except sqlite3.IntegrityError as e:
		print('The license code in combination with the publisher {} already exists.'.format(publisher_enter))
		print('Did not write to the database.')
		db.rollback()


def deleteLicense(db,cursor): 
	while(True):
		print("Enter 'p' if you want to delete a publisher. Or enter 'x' if you want to delete a license")
		choiche = input(">>")
		if choiche == 'p':
			show = executeQuery(cursor,"SELECT * FROM publisher")
			print(tabulate(show, headers=["Publisher", "Contactpersoon"]))
			to_delete = input("Please enter the name of the publisher you wish to delete:")
			cursor.execute('DELETE FROM publisher WHERE publisher_name = ?',(to_delete,))
			db.commit()
			break	

		elif choiche == 'x':
			
			result =executeQuery(cursor,"SELECT * FROM licenses")
			print(tabulate(result, headers=["License code", "Name", "Category", "Comments", "Publisher"]))
			to_delete = input("Please enter the name of the license you wish to delete:")
			cursor.execute('DELETE FROM license WHERE license_name = ?', (to_delete,))
			db.commit()
			break

		else:
			print("Please enter 'p' or 'x'.")
			continue


def main():
	db, cursor = connectToDatabase() # create the database connection anda cursor @ functions above.
	while(True):
		keuze = printMenu()
		if keuze == 1:
			addLicense(db,cursor)
			continue
		elif keuze == 2:
			addPublisher(db,cursor)
			continue
		elif keuze == 3:
			searchLicense(db,cursor)
			continue
		elif keuze == 4:
			deleteLicense(db,cursor)
			continue
		elif keuze == 5:
			pass
		elif keuze == 6:
			break
	db.close()# no matter what, always close your database
if __name__ == '__main__':
	main()
