#!/usr/bin/python3
from pymysql import connect, err, sys, cursors
def main():

	 conn = connect(host="localhost",
						user="root",
						passwd="casper",
						db="pytest")
	 cursor = conn.cursor(cursors.DictCursor)
	 # cursor.execute( """CREATE TABLE IF NOT EXISTS persoon
	 # 				(
	 # 				'ID' INT AUTO_INCREMENT NOT NULL,
	 # 				'voornaam' VARCHAR(100) NOT NULL,
	 # 				'achternaam' VARCHAR(100) NOT NULL,
	 # 				PRIMARY KEY('ID')
	 # 				)
	 # 				""" )
	 # cursor.execute("""CREATE TABLE 'persoon'
	 # 				(
	 # 				id int ,
	 # 				voornaam text,
	 # 				achternaam text,
	 # 				)""")
	 				
	#conn = connect(host="localhost",port = 3306, user="root", passwd = "casper", db="pytest")

	# cursor = db.cursor()

	 #cursor.execute("CREATE TABLE IF NOT EXISTS persoon(id int AUTO_INCREMENT PRIMARY KEY, naam varchar(100) NOT NULL, achternaam varchar(100) NOT NULL)")
	 #cursor.execute("CREATE TABLE persoon(id int, voornaam text, achternaam text)")
	 vnaam = input("Wat is uw naam?")
	 anaam = input("Wat is uw achternaam?")
	 cursor.execute("INSERT INTO persoon (naam, achternaam) VALUES(%s, %s)", (vnaam, anaam))
	 conn.commit()

if __name__ == '__main__':
	main()

