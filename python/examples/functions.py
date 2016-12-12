#functions
#functions
#~ def sum(x,y=10):
	#~ return x+y
	#~ 
#~ print(sum(10,10))
#~ print(sum(,10))
def stripe():
	print("---------------------")
def f(x):
	return x*2
print(f(3))
g = lambda x, f=12: x*2*f
print(g(3))

g = lambda x, y: x*y

h = 'Google' if g(2,2) < 55 else 'No'
print(h)
stripe()

def evenval(x):
	return x % 2 == 0
evens=filter(evenval, range(0,14))
print(list((evens)))

def square(x):
	return x*x
sqr = map(square, range(1,11))
print(list(sqr))
k=map( str, [ 5, 10.15, 20, 25.628, 7 ] )
print (list(k))
stripe()
items = [1,2,3,4,5]
print(list(map((lambda x: x **2), items)))
