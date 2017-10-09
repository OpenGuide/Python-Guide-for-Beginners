# This example uses python classes for addition

class Numbers(object):
  def __init__(self):
    self.sum = 0
  
  def add(self,x):
    # Addtion funciton
    self.sum += x 
  
  def total(self):
  # Returns the total of the sum
    return self.sum
  
  

if __name__ == "__main__":
  # Prints 12 on the terminal when the file is run,
  # you can even use input() to get numbers from
  # users.
  
  add = Numbers()
  add.add(5)
  add.add(7)
  y = add.total()
  print("Total Sum : " , y)
