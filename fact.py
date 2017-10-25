def fact(n):

	if n < 0:
		return("Error, factorial function is not defined for negative values")
	if n == 0:
		return 1

	return n*fact(n-1)

try:
	n = int(raw_input("Enter your number to factorize: "))
	print(fact(n))

except ValueError:
	print("You must enter an integer number!")
