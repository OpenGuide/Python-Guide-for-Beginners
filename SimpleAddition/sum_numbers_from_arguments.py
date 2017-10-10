'''
Python 3
Takes two numbers given as command line arguments, and prints their sum
'''

# The sys library lets us access command line arguments
import sys


# This line ensures the code will only run if the file is launched as a program - not if it is imported as a module
if __name__ == '__main__':
	
	# The sys.argv array contains the command passed to Python.
	# The first element is the name of the program, while the following elements are command-line arguments.
	# The float function converts the argument, which is a string, to a decimal number.
	x = float(sys.argv[1])
	y = float(sys.argv[2])
	
	# To get the sum of two numbers, we simply use the + operator
	sum = x + y
	
	# Finally, we print our result to the console
	print(sum)