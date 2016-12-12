#recursion
#when youre using recursion, remember to have an exit function to exit the loop.

def addseq(x):
	if x == 1: return 1
	else: return x + addseq(x-1)
print('The sum of the first 10 sequence numbers is', addseq(5))
