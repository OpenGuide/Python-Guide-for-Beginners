# Fibonacci Number is equal to 1 minus itself plus 2 minus itself:
# f(n) = f(n-1) + f(n-2)

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Showing the first 10 in the sequence
for i in range(10):
    print(fib(i))
