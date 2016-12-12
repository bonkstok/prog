#moreoop2.py
class student:
	def __init__(self,r,n):
		self.roll = r
		self.name = n

	def showStudent(self):
		print("Roll:", self.roll)
		print("Name:", self.name) 

class science(student):
	def __init__(self, r,n,p,c):
		student.__init__(self,r,n)
		self.physics = p
		self.chemistry = c

	@staticmethod
	def getGrade(x):
		if x < 55:
			return 'You have failed the class'
		elif x >= 55 and x < 80:
			return 'You have passed the class'
		elif x >= 80 and x <= 100:
			return 'You have raped the class' 
	def showScience(self):
		student.showStudent(self)
		print(self.getGrade(self.physics))
		print("Physics:", self.physics, ".",self.getGrade(self.physics))
		print("Chemistry:", self.chemistry,".", self.getGrade(self.chemistry))#end="**")

class arts(student):
	def __init__(self, r,n,h,g):
		student.__init__(self, r,n)
		self.history = h
		self.geography = g
	def showArts(self):
		student.showStudent(self)
		print("History:", self.history)
		print("geography:", self.geography)

stu = student("Teacher", "Henk")
scie = science("Student", "Ellies", 67, 70)
art = arts("Student", "Marjo", 70, 70)

print("Stu:")
stu.showStudent()
print("Scie:")
scie.showScience()
print("Arts")
art.showArts()