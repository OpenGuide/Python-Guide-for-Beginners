from math import factorial
from itertools import combinations

#This is a recursive implementation for generating Pascal's triangle.
def recursive(n):
	def recursive_row(n,k):
		if k == 0 or k == n:
			return 1
		return recursive_row(n-1, k-1) + recursive_row(n-1, k);
	triangle = [];
	for row in range(n):
		curr_row = [];
		for k in range(row+1):
			curr_row.append(recursive_row(row, k))
		triangle.append(curr_row)	

	return triangle

#This is the typical definition of Pascal's triangle.
def bruteForce_sumLast(n):
	triangle = []
	for row in range(n):
		curr_row = []
		for i in range(row+1):
			if i == 0 or i == row:
				curr_row.append(1);
			else:
				curr_row.append(triangle[-1][i-1]+triangle[-1][i])
		triangle.append(curr_row)
	return triangle

#We define the n choose k function: https://en.wikipedia.org/wiki/Combination
#This will be useful in the next function.
def nchoosek(n,k):
	#There are multiple ways of computing this aswell!
	#For example, it can be computed recursively or via the definition nCk = n!/(k!*(n-k)!)
	return len(list(combinations(range(n),k)))

#This is the definition of the Pascal's triangle using combinatorial numbers.
def bruteForce_factorial(n):
	triangle = []
	for row in range(n):
		curr_row = []
		for col in range(row+1):
			curr_row.append( nchoosek(row, col) )
		triangle.append(curr_row)
	return triangle


#This algorithm is taken from user MortalViews in StackExchange from the post 
#https://stackoverflow.com/questions/24093387/pascals-triangle-for-python
#This is just for visualization purposes!
#Just enter the output of any of the above functions and it will work.
def draw_beautiful(ps):
    max = len(' '.join(map(str,ps[-1])))
    for p in ps:
        print(' '.join(map(str,p)).center(max)+'\n')
