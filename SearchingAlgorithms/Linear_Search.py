def linearSearch(item, data):
  position = 0
  found = 0
  
  while position < len(data) and not found:
    if(data[position] == item):
      found = True
    position += 1
  return found
