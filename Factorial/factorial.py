# Factorial of a non-negative number is the product of all positive integers less than or equal to that number.
# For example: 5! = 5 x 4 x 3 x 2 x 1 = 120
# 0! = 1 

# Using a recursive function: 
def factorial(n):
    """Takes a number and returns the factorial value"""

    if n <= 1:
        return 1
    
    return n * factorial(n - 1)
