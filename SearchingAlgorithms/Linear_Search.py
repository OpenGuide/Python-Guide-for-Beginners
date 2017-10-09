def linear_search(list,searched_element):
    for i in range(len(list)):
        if(list[i]==searched_element):
            print("The item was found at index "+i)
            return i
    print("The item was not found in the list")
    return False
