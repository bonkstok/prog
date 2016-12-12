#test file for pdf 
p = [0 for i in range(5)]
print(len(p))
p.append(input("Geef een cijfer voor de array:"))
print(p)
print(len(p))
for i in range(6):
	p[i] = 0
#del p[:]
print(p)
print("Enter five numbers")
for i in range(len(p)):
	p.append(int(input("Geef de data voor index[" + str(i) + "] :")))
print(p)
