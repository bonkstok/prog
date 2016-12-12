
def sum (a=10,b=5):
	"Adds the two numbers"
	return a + b
sum.version = "1.0"
sum.author= "Johnny"
k=sum(10,20)
print('The documentation string is {}'.format(sum.__doc__))
print('The function name is {}'.format(sum.__name__))
print('The default values of the functions are', sum.__defaults__)
print('The code of the function is', sum.__code__)
print('The dictionary of the function is', sum.__dict__)
