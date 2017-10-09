
# first lets get 2 numbers to add
print "enter 2 number to add"

# getting the first number
number1 = raw_input("Ok enter the first number ")

# and now the second number
number2 = raw_input("and now the second number ")

# finally calculating the addidition of the numbers
# sum = number1 + number2
# seems to be right
# but as the inputs are taken as string we need to type cast them
# that is convert number1 and number2 to integer from string
# so lets do that

number1 = int(number1)
number2 = int(number2)
# and now lets calculate the sum
sum = number1 + number2

# and now lets print the numbers
print "the addition of the 2 numbers is "
print sum

