#generators
# to be a generator, the function must return a value using the yield keyword
#the generator function uses the yiel keyword to get the next value in the container

def fruits(seq):
	for fruit in seq:
		yield str(fruit)

f = fruits(['Apple', 'Orange', 'Mango', 'Banana'])
print('The list of fruits is:')
for x in f:
	print(x)
#same as
f = fruits(['Apple', 'Orange', 'Mango', 'Banana'])
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
# when you reach the end and you try to iterage again, you will get a 'StopIteration'
#error.

#generator expressions
def squarenum(x):
	return x*x

iteratorobj = (squarenum(x) for x in range(6))
print(iteratorobj)
print(iteratorobj.__next__())
print(iteratorobj.__next__())
print(iteratorobj.__next__())
print(iteratorobj.__next__())
print(iteratorobj.__next__())
print(iteratorobj.__next__())

#same as
iteratorobj = (squarenum(x) for x in range(6))
for obj in iteratorobj:
	print(obj)
