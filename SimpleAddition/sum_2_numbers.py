'''
Inputs a string, uses the split() function to remove whitespaces
and then uses map() function to map them to integers.
'''
a,b = map(int, input("Enter two numbers: ").split())
'''
Outputs the sum after using a format specifier %d 
to denote a placeholder for an integer.
'''
print("The sum is %d\n"%(a+b))