import csv
import sqlite3

to_add = []
with open('testsheet.csv') as csvfile:
 	read_csv = csv.reader(csvfile)
 	next(read_csv, None)# skip the headers
 	for row in read_csv:
 		to_add.append((row[0], row[1],row[2],row[3],row[4]))


# for it in to_add:
# 	print(it)
# # 	for part in it:
# # 		print(part)
# # 	#print(it)

db = sqlite3.connect('license_test.db')
cursor = db.cursor()

cursor.executemany("INSERT INTO license VALUES(?,?,?,?,?)",(to_add))
db.commit()

# #cursor.executemany("""INSERT INTO USERS(name, phone,email,password)
# # #					VALUES(?,?,?,?)""",(add))
# data = []
# with open('testsheet.csv') as csvfile:
# 	writer = csv.writer(csvfile)
# 	writer.writerow(['Column 1,Column 2,Column 4,Column 4,Column 5'])
# 	writer.writerows(data)