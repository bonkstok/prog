#moreoop
#from __future__ import division 
class worker:
	def __init__(self,c,n,s):
		self.code = c
		self.name = n
		self.salary = s
	def showworker(self):
		print("Code is:\t",self.code)
		print("Name is:\t",self.name)
		print("Salary is:\t",self.salary)
	def getName(self):
		return self.name
class officer(worker):
	def __init__(self,c,n,s):
		worker.__init__(self,c,n,s)
		self.hra = s*60/100
	
	def showOfficer(self):
		worker.showworker(self)
		print("HRA:\t\t",self.hra)
class manager(officer):
	def __init__(self,c,n,s,da):
		officer.__init__(self,c,n,s)
		self.da = da
	def setDa(self, da):
		self.da = da
	def getDa(self):
		return self.da
	def showManager(self):
		officer.showOfficer(self)
		print("DA:\t\t", self.da)
	dat = property(setDa,getDa)

w = worker(101,'John', 2000)
o = officer(102,'David', 4000)
m = manager(103,'Ben', 5000, 2500)
print('Worker:')
w.showworker()
print('Officer:')
o.showOfficer()
print(o.getName())
print('Manager:')
m.showManager()
print("Here are the names")
print(w.getName())
print(o.getName())
print(m.getName())
print(m.da)
m.da = 5000
print(float(m.da))
print(m.da)
