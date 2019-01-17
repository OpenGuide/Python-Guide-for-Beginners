c=1
for i in range(1,int(input('Enter Number of rows :'))+1):
    list1=[]
    for j in range(i):
        list1+=[str(c)]
        c+=1
    print ' '.join(list1)
