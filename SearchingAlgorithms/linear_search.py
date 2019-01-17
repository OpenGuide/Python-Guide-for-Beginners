import random
#Searches for an item inside listint, a list of integers
#and returns the position at which element is found
def linear_search(listint,item):
	for index,elem in enumerate(listint):
		if elem==item:
			return index+1
	return -1		

#Generate 100 Random Integers
randomarray = [random.randint(0,100) for j in range(100)]		
item = int(input("Enter item to find: "))
#Calls linear_search() on the generated random array and checks if item is there
index = linear_search(randomarray,item)
if index==-1:
	print("Not Found")
else:
	print("The item was found at position {}".format(index))