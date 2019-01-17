### Sum all integers numbers between 0 to 10 included

# Create 2 variables, one to keep the result(sum) and another to count(i)


sum=0  ### sum is the variable where the value of 0+1+2+3+4+5+6+7+8+9+10 will be added .
i=0    ### i is the counter, so we could add the value to the sum.

# Create a loop using while(condition): 
                        # calculation

while (i<=10):
    ### sum receive the anterior value of sum plus the value of i
    
    sum=sum+i
    
    ### In this line we increase the value of i , another form to write is i=i+1
    
    i+=1 

# print the result in the screen

print (sum)

