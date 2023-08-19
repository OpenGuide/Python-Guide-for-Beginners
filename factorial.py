# Python program to find the factorial of a number

def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Enter the number:"))
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
else:
    print(factorial(num))
