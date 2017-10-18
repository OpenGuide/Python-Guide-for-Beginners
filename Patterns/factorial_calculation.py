# recursively finds the factorial of a number
def factorial(number):
    if number == 0:
        return 1
    else:
        return factorial(number - 1) * number

print(factorial(20))
