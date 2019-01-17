
'''
This code asks the user to input a non-negative integer and then returns the factorial
'''


#Solicit user input until a non-negative integer is provided
while True:
  try:
    input_num = input("Enter a non-negative integer: ")
    
    #The user should not enter a negative number or a non-integer
    if (input_num<0) | (type(input_num)!=int):
      print("Invalid entry\n")
      continue
    
    break
  
  #The user should not enter anything else besides a non-negative integer (e.g. strings)
  except Exception as e:
    print("Invalid entry\n")



#Calculate the factorial expression as follows:
#1*2*...*input_num
result = 1
for i in xrange(1,input_num+1):
  result*=i


  
print("{}! = {}".format(input_num, result))

