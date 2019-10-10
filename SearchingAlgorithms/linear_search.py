n=[i for i in input("Enter Elements:").split()]
s=input("Search Element:")
t=0
for i in n:
    if(s==i):
        t=1
if(t==0):
    print("Element not Found")
else:
    print("Element Found")
