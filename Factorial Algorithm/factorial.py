print("This program calculates the factorial of the given number")
n = int(input("Enter the number for which factorial is to be calculated:"))
fact = 1
for i in range(1,n+1):
	fact = fact*i
print("Factorial of",n,"is",fact)
input()