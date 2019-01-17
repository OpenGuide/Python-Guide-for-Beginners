# A simple program that asks the user for input from console
# as integers and returns the sum of the two.
# This program validates the input from the user.
#
# INPUT: x, y where x, y are two integers
# OUTPUT: z, where z is the sum of x and y.
#
# @author: Alvin Nguyen
promptFirstNumber = "Enter the first number: "
promptSecondNumber = "Enter the second number: "
errorMessage = "The number you entered is not an integer."

print("This program prompts you for two integer numbers, and outputs the sum of the two.")
while True:
    try:
        x = int(input(promptFirstNumber))
    except ValueError:
        print(errorMessage)
        x = input(promptFirstNumber)
    else:
        break;

while True:
    try:
        y = int(input(promptSecondNumber))
    except ValueError:
        print(errorMessage)
        y = input(promptSecondNumber)
    else:
        break;

print(x + y)



