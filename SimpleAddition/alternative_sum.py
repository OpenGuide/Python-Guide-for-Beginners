try:
	x = float(raw_input("Enter first number: "))
	y = float(raw_input("Enter second number: "))

	result = x+y
	print('Result: ' + str(result))

except ValueError:
	print("Error. Input cannot be interpreted as a number")
