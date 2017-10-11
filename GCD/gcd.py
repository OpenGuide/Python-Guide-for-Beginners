def gcd_recursive(a, b):
    """
    Function to compute the greatest common denominator
    of two numbers using Euclids algorithm recursively
    """
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


def gcd(a, b):
    """
    Function to compute the greatest common denominator
    of two numbers using Euclids algorithm iteratively
    """
    while b > 0:
        a, b = b, a % b
    return a


a = input("Enter first number: ")
b = input("Enter second number: ")

print "Greatest Common Denominator is %d" % gcd(a, b)
