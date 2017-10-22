# recursively finds the factorial of a number using user input
def factorial(number):
    if number == 0:
        return 1
    else:
        return factorial(number - 1) * number
        
x = int(input().strip())
print(factorial(x))
