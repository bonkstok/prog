#testclass
import sqlite3 
import os
import csv
from sys import exit
from tabulate import tabulate

class dbmanager(object):
	
	def __init__(self, database):
		if not os.path.isfile(database):
			print("Creating database")
			self.__db = sqlite3.connect(database)
			self.__cursor = self.__db.cursor()
			self.createSchema()
		else:
			self.__db= sqlite3.connect(database)	
			self.__cursor = self.__db.cursor()		
		
	def createSchema(self):
		publisher_ini = "CREATE TABLE IF NOT EXISTS publisher(publisher_name TEXT PRIMARY KEY , contactpersoon TEXT)"
		license_ini ="CREATE TABLE IF NOT EXISTS license(license_code TEXT NOT NULL, license_name TEXT NOT NULL, license_cat TEXT NOT NULL,license_comment TEXT, publisher_name TEXT NOT NULL, FOREIGN KEY(publisher_name) REFERENCES publisher(publisher_name), PRIMARY KEY(license_code, publisher_name))"
		self.__cursor.execute(publisher_ini)
		self.__cursor.execute(license_ini)
		self.__db.commit() 	
		print("Done....")

	def printMenu(self):
		print("1. Add license.")
		print("2. Add publisher.")
		print("3. Search license.")
		print("4. Delete publisher or license.")
		print("5. Import licenses from a .csv file.")
		print("6. Export licenses to PDF")
		print("7. Quit.")
		try:
			keuze = int(input(">>>"))
			return keuze
		except ValueError:
			print("Please enter a number![1:6].")


	def __selectQuery(self, query):
		self.__cursor.execute(query)
		return  self.__cursor.fetchall()


	@staticmethod
	def checkStringNotEmpty(text_input):
		while(True):
			to_return = input(text_input)
			if not to_return:
				continue 
			else:
				return to_return
				break

	def addLicense(self):
		license_code = self.checkStringNotEmpty("Enter the license code:")
		license_name = self.checkStringNotEmpty("Enter the software-package name:")
		license_cat  = self.checkStringNotEmpty("Enter license category:") #Still not sure whether cat can be NULL or not.
		comments = input("Comments:") #This can be null, hence why function checkString is not called.
		self.__cursor.execute("SELECT publisher_name FROM publisher")
		print(tabulate(self.__cursor.fetchall(), headers=["Publisher"]))
		publisher_enter = self.checkStringNotEmpty("Please one of the publishers displayed above:")
		
		try:
			self.__cursor.execute("INSERT INTO license VALUES(?,?,?,?,?)",(license_code,license_name, license_cat, comments, publisher_enter))
			self.__db.commit()
		except sqlite3.IntegrityError as e:
			print('The license code in combination with the publisher {} already exists.'.format(publisher_enter))
			print('Did not write to the database.')
			self.__db.rollback()	


	def addPublisher(self):
		name_pub = self.checkStringNotEmpty("Please enter the name of the publisher:") #Cannot be null
		contactpersoon_pub = self.checkStringNotEmpty("Please enter the name of the contactperson:") #Can be null, preferable not.  

		add = [(name_pub, contactpersoon_pub)]
		print(add)
		try:
			self.__cursor.execute("""INSERT INTO publisher(publisher_name, contactpersoon)
						VALUES(?,?)""",(name_pub, contactpersoon_pub))
			self.__db.commit()
		except sqlite3.IntegrityError as e:
			print(e)
			print('Publisher {} already exists. Did not write to database.'.format(name_pub))
			self.__db.rollback()


	def deleteLicense(self): 
		while(True):
			print("Enter 'p' if you want to delete a publisher. Or enter 'x' if you want to delete a license")
			choiche = input(">>")
			if choiche == 'p':

				show = self.__selectQuery("SELECT * FROM publisher")
				#show = executeQuery(cursor,"SELECT * FROM publisher")
				print(tabulate(show, headers=["Publisher", "Contactpersoon"]))
				to_delete = input("Please enter the name of the publisher you wish to delete:")
				self.__cursor.execute('DELETE FROM publisher WHERE publisher_name = ?',(to_delete,))
				self.__cursor.execute('DELETE FROM license WHERE publisher_name = ?', (to_delete,)) # delete because of the relationship. many to one. When the one gets deleted all the licenses get deleted from that publisher get deleted.
				self.__db.commit()
				break	

			elif choiche == 'x':
				print("You can delete more if you seperate the license names by a comma(no spaces).")
				result = self.__selectQuery("SELECT * FROM license")
				print(tabulate(result, headers=["License code", "Name", "Category", "Comments", "Publisher"]))
				to_delete = input("Please enter the name of the license you wish to delete:")
				to_delete = to_delete.split(',')
				self.__cursor.executemany('DELETE FROM license WHERE license_name = ?', (to_delete,))
				self.__db.commit()
				break
			else:
				print("Please enter 'p' or 'x'.")
				continue
	

	def searchLicense(self):
		search = input("Search:")
		self.__cursor.execute("SELECT * from license WHERE publisher_name LIKE ? or license_cat LIKE ? or license_name LIKE ?",('%'+search+'%','%'+search+'%','%'+search+'%'))#the % are wildcards. 
		result = self.__cursor.fetchall()
		print(tabulate(result, headers=["License code", "Name", "Category", "Comments", "Publisher"]))#tabulate is a package that outputs a nice format list.


	def importCsv(self):
		file = input("Please enter the name of your .csv file:")
		to_add = []
		with open(file+'.csv') as csvfile:
			read_csv = csv.reader(csvfile)
			next(read_csv, None)# skip the headers
			for row in read_csv:
				to_add.append((row[0], row[1],row[2],row[3],row[4]))
		try:
			self.__cursor.executemany('INSERT INTO license VALUES(?,?,?,?,?)',(to_add))
			self.__db.commit()
			print("Succesfully imported the file:{}".format(file+'.csv'))
		except sqlite3.IntegrityError as e:
			print('There is already a combination of license + publisher in the database.')
			print('Not writing to database.')
			self.__db.rollback()


	def exportCsv(self):
		self.__cursor.execute("SELECT * FROM license")
		result = self.__cursor.fetchall()
		name = input('Please give a file name:')
		with open(name+'.csv', 'wt') as csvwrite:
			a = csv.writer(csvwrite)
			a.writerow(('Code', 'Name', 'Category', 'Comment', 'Publisher'))
			a.writerows(result)


	def addPublisher(self):
		name_pub = self.checkStringNotEmpty("Please enter the name of the publisher:") #Cannot be null
		contactpersoon_pub = self.checkStringNotEmpty("Please enter the name of the contactperson:") #Can be null, preferable not.  
		add = [(name_pub, contactpersoon_pub)]
		print(add)
		try:
			self.__cursor.execute("""INSERT INTO publisher(publisher_name, contactpersoon)
						VALUES(?,?)""",(name_pub, contactpersoon_pub))
			self.__db.commit()
		except sqlite3.IntegrityError as e:
			print(e)
			print('Publisher {} already exists. Did not write to database.'.format(name_pub))
			self.__db.rollback()

	def __del__(self):
		print("Closing db.")
		self.__db.close()


def main():
	db_instance = dbmanager('license_test.db')
	while(True):
		keuze = db_instance.printMenu()
		if keuze == 1:
			db_instance.addLicense()
			continue
		elif keuze == 2:
			db_instance.addPublisher()
			continue
		elif keuze == 3:
			db_instance.searchLicense()
			continue
		elif keuze == 4:
			db_instance.deleteLicense()
			continue
		elif keuze == 5:
			db_instance.importCsv()
		elif keuze == 6:
			db_instance.exportCsv()
			continue
		elif keuze == 7:
			exit()

if __name__ == '__main__':
	main()