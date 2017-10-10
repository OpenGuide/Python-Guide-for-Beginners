from functools import reduce

'''
Recursively multiply Integer with its previous integer (one less than current number) until the number reaches 0, in which case 1 is returned
'''
def recursive_factorial(n):

	# Base Case: return 1 when n reaches 0
	if n == 0 :
		return 1
	# recursive call to function with the integer one less than current integer	
	else:
		return n * recursive_factorial(n-1)

'''
Iterative factorial using lambda and reduce function, from range 1 to number + 1 we multiply all the numbers through reduce.
'''
def iterative_factorial(n):
	factorial = reduce(lambda x,y:x*y,range(1,n+1))
	return factorial


# Taking number from standard input and casting it into Integer
n = int(input("Enter the number: "))

# Taking in Calculation stratergy(recursive/iterative) and removing trailing spaces and changing to lowercase
stratergy = input("Enter algorithm type (r for Recursive/i for iterative): ").strip().lower()

# Just a check to see if right option was entered
if(stratergy != "r" and stratergy !="i"):
	print("wrong algorithm type opted...exiting")
	quit()

# Factorial by opted stratergy
if(stratergy == "r"):
	factorial = recursive_factorial(n)

elif(stratergy == "i"):
	factorial = iterative_factorial(n)


print("Factorial of entered number is: ",str(factorial))