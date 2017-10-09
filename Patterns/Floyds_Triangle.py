def printTriangle(r):	# function to print triangle, given a row
	count = 1;	# running total of numbers to print
	columns = 1	# number of columns per row (increases by 1 each row)
	for i in range(0, r):	# iterates through rows
		for j in range(0, columns):	# iterates through columns per row
			print (count, " ", end="")	# prints the current count + a space
			count += 1	# count increases every number
		print()	# this is needed for a newline (new row)
		columns += 1	# increases number of columns each row

def main():	# main function, takes numerical row input
	rows = int(input("Enter number of rows of Floyd's Triangle to print: "))
	printTriangle(rows)

if __name__ == "__main__":
    main()