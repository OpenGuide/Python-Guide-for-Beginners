# Linear search function that returns 'True' if the item is in the list 'data' of 'False' otherwise

def linearSearch(item, data):
  # Start with position 0 and not found the element yet
  position = 0
  found = False
  
  # Check if item is in the list from position 0 to the end of the list
  # When element is found, change the value of the variable 'found' to 'True'
  while position < len(data) and not found:
    if(data[position] == item):
      found = True
    position += 1
    
  return found
