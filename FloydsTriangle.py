def floyd(n):
    k=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(k,end=' ')
            k=k+1
        print()
    return
n=int(input("Enter the number of rows you want to print in Floyd's Triangle:\n"))
print()
floyd(n)
    
