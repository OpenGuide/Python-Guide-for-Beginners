#To find factorial
c='y'
while c=='y' or c=='Y':
    i=0
    f=1
    n=int(input("Enter no:"))
    while i<n:
        f*=(n-i)
        i+=1
    print(f)    
    c=input("Continue(y/n):")
print("BYE :)")
