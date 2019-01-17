# Python program to find the factorial of a given number

# input the number to find its factorial
num = int(input("Enter a number: "))

factorial = 1

if num < 0:			#factorial doesn't exist for a negative number
   print("Please enter a valid number!")

elif num == 0:		#factorial of 0 is 1
   print("The factorial of 0 is 1")

else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print "The factorial of",num,"is",factorial