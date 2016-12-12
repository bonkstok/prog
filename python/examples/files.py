#files
matter = '''Python is a great language.
Easy to understand and learn.
Supports OOP.
Also used in webdevelopment.'''

# def isOpen(x):
# 	if x == 'r':
# 		return 'read'
# 	elif x == 'w':
# 		return 'write'
# 	elif x == 'w+':
# 		return 'read and write'
f = open('testfiles.txt', 'w')
f.write(matter)
f.close()
f = open('testfiles.txt', 'r+')
while True:
	line = f.readline()
	if len(line) == 0:
		break
	print(line,)
f.close()
# print("This is the content of the file {}".format(f.name))
# print("Is it currently closed? ",f.closed)
# print("Is it opened in the mode: ", isOpen(f.mode))
# print(f.mode)
# print('File number descriptor is:', f.fileno())
# f.close()
# print("Is it closed now? ", f.closed)
#del f
print('--------------------------------')
f = open('testfiles.txt', 'r')
lines = f.read()
print(lines)
f.close()
f = open('testfiles.txt', 'r+')
print("Deleting content of:", f.name)
f.truncate()
print("File is empty.")
toadd = []
while(True):
	tovoeg = input("Enter a line for add to the file {}\n".format(f.name))
	toadd.append(tovoeg)
	print("press y to enter another line.")
	cont = input(">>>")
	if cont == 'y':
		pass
	else:
		break
for sentence in toadd:
	f.write("\n{}".format(sentence))