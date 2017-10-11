# Most python newbies may not be knowing about decorators
# They are inbuit python funcitons also know as magic function
# They have a general format like __self__ , __SOMETHING__ etc.

# So for this script we'll be using Pyhton decorators to add
# numbers

# 1. Simple Addition
print (5).__add__(7) # prints 12

print (2).__add__(1) # prints 3

# 2. Functions

class Number(int):
'''
  i have not use '+' to add self and other as '+' references to 
  __add__ , hence it would create an infinite recursion.
  So we used two '-' to add the two numbers.
'''
  def __add__(self, other):
        return self - (-other)

print Number(5) + 3 # Prints 8 

