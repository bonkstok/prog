class Animal:
	
	def talk(self):
		print("I have something to say")
	def walk(self):
		print("Hey im walking here")
	def clothes(self):
		print("Im wearing clothes")



class Duck(Animal):
	
	def quack(self):
		print("Quaaack!")

	def walk(self):
		super().walk()

	def printSuper(self):
		super().printNaam()
		print(self._name)




def main():
	donald = Duck()
	donald.clothes()
	donald.walk()


if __name__ == '__main__':
	main()