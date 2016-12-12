#binaryfiles
import pickle
str = 'Hello world'
f = open('filebinary.bin', 'wb')
f.write(str.encode('utf-8'))
f.close()
f = open('filebinary.bin', 'rb')
fcontent = f.read()
f.close()
print(fcontent)
print(fcontent.decode('utf-8'))

"""Serialization (pickling)"""
#Serialization is done when storing data
#deserialization is done when retrieving data. 
#you can use Pickle or cPickle(written in C)
# class rect:
# 	def __init__ (self, x,y):
# 		self.l = x
# 		self.b = y
# 	def rectarea(self):
# 		return "Area of rectangle is", self.l * self.b

# r = rect(5,8)
# f = open('studentinfo.bin', 'wb')
# pickle.dump(r,f) #dump r into f
# f.close()
# del r
# f = open('studentinfo.bin', 'rb')
# storedobj = pickle.load(f)
# print(storedobj.rectarea())

class user:
	def __init__(self,id,name,email):
		self.id = int(id)
		self.name = name
		self.email = email
		

	def dispuser(self):
		#print(self.id)
		if self.id == 0:
			print("Invalid ID givin for person: {}. Please enter a valid id (1-x)".format(self.name))
		else:
			print('User ID:', self.id)
			print('User Name:', self.name)
			print('Email address:', self.email)


f = open('UsersInfo.bin', 'wb')
n = int(input("How many users? "))
print('Enter', n ,'numbers')
for i in range(0,n):
	u = input('User ID:')
	n = input('User Name:')
	e = input('Email address:')
	usrobj=user(u,n,e)#create instance of class
	pickle.dump(usrobj,f)#dump values into .bin file
f.close()
f = open('UsersInfo.bin', 'rb')
print("Printing users:")
while True:
	try: 
		usrobj = pickle.load(f)
	except EOFError:
		break
	else:
		usrobj.dispuser()
f.close()





