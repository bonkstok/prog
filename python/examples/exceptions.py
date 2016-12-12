"""
Syntax
try:
	statements(s)
except someException:
	code for handling someException
"""
try:
	x = int(input('x:'))
	y = int(input('y:'))
	print(x / y)
except ZeroDivisionError:
	print("You can not have division 0!")
arr = [1,2]
try:
	print(arr[2])
except IndexError:
	print("Out of range")
n = int(input('Enter a positive value:'))
assert(n >= 0), "Entered value is not a positive value!"