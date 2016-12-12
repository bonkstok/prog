import sys
print("There are {} cli-arguments.".format(len(sys.argv)))
print("The arguments being:")
for i in sys.argv:
	print(i)
print("Python version: {}. The path to this version is:{}.".format(sys.version, sys.path))
print(sys.thread_info)
