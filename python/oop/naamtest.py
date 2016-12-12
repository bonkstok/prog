
def getName():
	print("Geef uw naam")
	naam = input(">>")
	return naam

def main():
	naam = getName()

	while not naam:
		print("You have to provide a name!")
		naam = getName()

	print("Welcome {}. Your name is of the type: {}".format(naam, type(naam)))
	a = 6
	b = 5
	c = "Less than" if a < b else "Greater than"
	print("A is {}  b".format(c))

if __name__ == '__main__':
	main()