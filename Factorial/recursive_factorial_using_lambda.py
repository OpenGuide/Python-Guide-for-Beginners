#Python program to find factorial of a number recursively
#This makes use of 'lambda' or anonymous functions

factorial = lambda x: x and x * factorial(x - 1) if x > 0 else 1

n = int(input('Enter a number:'))

print(('Factorial of '+ str(n) + ' is ' + str(factorial(n))) if not n < 0 else 'Enter a valid input')
