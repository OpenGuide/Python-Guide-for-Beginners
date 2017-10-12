# Merge Sort implements divide and conquer mechanism to sort the given list of numbers.
# The unsorted list is divided into two parts recursively until only one element is left.
# These single element lists are then compared and merged together in a sorted order.  

# This function merges two lists list1 and list2 in sorted order and returns the merged list.
def merge(list1,list2):
    merged_list = []
    #while len(list1) != 0 and len(list2) != 0:
    while list1 and list2:
        # Loop until both the lists are not empty
        if(list1[0] < list2[0]):
            merged_list.append(list1[0])
            list1.pop(0)
        else :
            merged_list.append(list2[0])
            list2.pop(0)    

    if not list1:
        merged_list += list2
    else :
         merged_list += list1
    
    return merged_list

# This function divides the unsorted list recursively and calls the merge function on two unsorted lists.
def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1 :
        return unsorted_list
    else:
        mid = int(len(unsorted_list)/2)
        list1 = merge_sort(unsorted_list[:mid])
        list2 = merge_sort(unsorted_list[mid:])
        return merge(list1,list2)

if __name__ == "__main__":
    print("Enter numbers to be sorted (seperated by space)")

    input_list = [int(x) for x in input().split()]
    # input() is similar to raw_input() in Python 2.x. 
    # This accepts the user input and splits it with spaces.
    # Each of the input numbers are then converted into an integer and added to the list input_list.
    
    sorted_list = merge_sort(input_list)
    # call merge_sort function on the received unsorted list from the user.

    print(sorted_list)
