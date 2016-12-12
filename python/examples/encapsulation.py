#encapsulation
# class Car:
# 	def __init__(self):
# 		self.__updateSoftware()
# 	def drive(self):
# 		print('Driving')
# 	def __updateSoftware(self):
# 		print('updating software')

# redcar = Car()
# redcar.drive()
# redcar.__updateSoftware()
class Car:
	__test = ""
	def __init__(self):
		self.__maxspeed = 200
		self.__name = "Supercar"
		self.__test = "TEST"
	def drive(self):
		print("Driving with the car {} at his maxspeed of {}.".format(self.__name, self.__maxspeed))
		print(self.__test)
	def setMaxSpeed(self, speed):
		self.__maxspeed = speed
	@property
	def name(self):
	    return self.__name
	@name.setter
	def name(self, naam):
		self.__name = naam
	
	# def s_etName(self, name):
	# 	self.__name = name
	# def getName(self):
	# 	return self.__name
	# name = property(getName, setName)
test = Car()
test.drive()
print(test.name)
test.name = 'Truck'
print(test.name)
print(test.name)
#print(test.getName())
#test.__name = "Jantje"
#print(test.getName())
test.__test = "Jantje"
test.__maxspeed = 500
test.drive()
print(test.__test)
test.drive()