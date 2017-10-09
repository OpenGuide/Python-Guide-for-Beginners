# python code to add two numbers
print("Add two numbers that you want to add. (space separated)")

""" map function in order to store the values of the two space separated integers
	map (function, iterable..) applies the function on all the items of the iterable """

a, b = map(int, raw_input().split()) # enter two space separated integers

print("The sum of the two numbers is : " + (str) (a +b))                         # displays the sum of the two integers
