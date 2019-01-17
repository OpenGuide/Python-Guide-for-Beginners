# -*- coding: utf-8 -*-


l = map(int, raw_input().split())   #enter space separated entries in a list
item = input("Enter some numbers: ")                      #item to be searched for
found = 0                           #check to find if th eitem has been found or not

for i in range(len(l)):
    if(l[i] == item):
        found = 1
        print('Item found in the list at index position : ' + str(i)) 
        break
    if(found == 0):
        print("Sorry, Item not found in the list ")
        
    
   
   
