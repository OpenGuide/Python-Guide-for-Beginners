'''
This is a program to find the sum of 'n' numbers given by the user.
We'll see the use of two different methodology : 1st => using list 
                                                 2nd => using for loop   
'''

# *****************
# First Methodology
# *****************


#Defining numbers' array(list) with 'arr' as the name 
arr = []


#number of numbers
n = int(input("How Many Numbers will you enter ? "))


#loop to get all numbers and add them to the array list
for i in range(1,n+1):

    #take the number from user and store it in a temporary variable 'inp'
    inp = int(input("Enter the {0} number : ".format(i)))
    
    #adding the given value to our list 
    arr.append(inp)

# Finally get the result using the  sum function which returns the addition of all contents of a list (any interable) 
print("Sum : " + str(sum(arr)))


# ***********************************
# 2nd Methodology using for loop: 
# ***********************************


#number of inputs
n = int(input("How Many Numbers will you enter ?"))


#intitializing a temporary variable to store the sum
s = int()


#loop to get all numbers and keep adding them to a variable
for i in range(1,n+1):
    
    # Getting the number from user
    inp = int(input(f"Enter the {i} number : "))

    # Add the input vale to the given variable    
    s += inp # equivalent to sum = sum + inp


print("Sum : "+ str(s))