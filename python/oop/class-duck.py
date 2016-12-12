class Duck:

	#constructor. This will always be executed when creating an instance of this class(object)
	def __init__(self, color = 'white'):
		self._color = color # the _ means that this is a local variable
		
	def quack(self):
		print("Quaaack!")

	def walk(self):
		print("Walks like a duck")

	@property
	def color(self):
		return self._color

	@color.setter
	def color(self, value):
		self._color = value

	def kindOfDuck(self):
		return "Your duck has the color {}".format(self._color)

def main(): 
	donald = Duck()
	donald.quack()
	donald.walk()
	print(donald.kindOfDuck())
	donald.color = "blue"
	print(donald.kindOfDuck())
	print(donald.color)
	donald.color="black"
	print(donald.color)

	

if __name__ == '__main__':
	main()