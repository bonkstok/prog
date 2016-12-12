#~ dict = {'Nederland':'Amsterdam', 'Duitsland':'Berlijn', 'Frankrijk':'Parijs', 'België': 'Brussel'}
#~ n = input("Enter a country:")
#~ if n in dict:
	#~ print("The capital of {} is {}.".format(n, dict[n]))
#~ 
#~ for land, hoofdstad in dict.items():
	#~ print("De hoofdstad van {} is {}".format(land, hoofdstad))
#~ 

student1 = {'John':60, 'Kelly':70, 'Caroline':90, 'Idioot':60, 'Henk':60, 'Margriet':50}
failed = ['Henk', 'Hoplo', 'Margriet']
back= {}
#print(failed)
student2 = dict([('David', 90), ('John', 55)])
#print('Items student1:\t', student1.items())
#print('Keys student1:\t', student1.keys())
#print('Values student1\t:', student1.values())
delete = []

#minimal = 50
#if minimal in student1.values():
#	print("Atleast someone failed this class")
highest = [0,0]
for name,grade in student1.items():
	#print(name)
	if name in failed:
		print('Sorry, {} is not allowed to enter this class.'.format(name))
	#	print('BTW, your grade WAS:{}'.format(grade))
		delete.append(name)
		#continue
	if grade > 50 and name not in delete:
		#print(highest[0])
		if grade > highest[0]:
			highest[0],highest[1] = grade, name
		print("{} has completed this course, with a grade of:{}".format(name,grade))
	
	
	#~ for name,mark in student1.items():
		#~ if mark > 50 and name not in delete:
			#~ print("{} has completed this course, with a grade of:{}".format(name,mark))
print("{} is the highest score. It belongs to {}".format(highest[0], highest[1]))		
print(delete)
print("There are curently {} students in the result variable".format(len(student1)))
verwij = 0
for name in delete:
	print('Deleting {} from the results'.format(name))
	del student1[name]
	verwij+= 1
print(student1)
print("{} studenten verwijderd".format(verwij))
#print(len(student1))
