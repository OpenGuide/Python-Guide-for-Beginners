'''
Takes two space-separated numbers as input using
split() to split at a whitespace and
map() to map the values to integers.
'''
a,b = map(int, input("Enter two numbers: ").split())
'''
Prints the sum of the two numbers using + arithmetic operator 
and %d as an integer format specifier.
'''
print("The sum is %d\n"%(a+b))