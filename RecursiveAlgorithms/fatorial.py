def fatorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return fatorial(n-1)*n

n = int(input("Please, enter the numb: "))
fatorial(n)
print(fatorial(n))
