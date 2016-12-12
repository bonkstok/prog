#tuples.
#ar = [0 for i in range(2)]
#myna = "Johnny"
#myage= 5
#ar[0],ar[1] = myna,myage
#print(ar)
tup = ('Roos', 'Pucky', 'Casper', 'Dolly', 'Joris', 'Plurk')
print('Displaying tuple entries:')
for name in tup:
	print(name)
print('Enter a name to search')
search = input('>>')
if search in tup:
	print("{} is found in the tuple. To be precize, is it at the index {}.".format(search, tup.index(search)))
else:
	print("{} is not found in the tuple.".format(search))
