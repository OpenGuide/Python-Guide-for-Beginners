# Python program to find the factorial of a number using recursion


#Function to return the factorial of a number using recursion
def recursiveFactorial(n):
   
   if n == 1:
       return n
   else:
       return n*recursiveFactorial(n-1)

# input the number to find its factorial
num = int(input("Enter a number: "))

if num < 0:				#factorial doesn't exist for a negative number
   print("Please enter a valid number!")

elif num == 0:			#factorial of 0 is 1
   print("The factorial of 0 is 1")

else:
   print "The factorial of",num,"is",recursiveFactorial(num)