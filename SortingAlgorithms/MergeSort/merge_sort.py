def merge(list1,list2):
    merged_list = []
    while len(list1) != 0 and len(list2) != 0 :
        if(list1[0] < list2[0]):
            merged_list.append(list1[0])
            list1.remove(list1[0])
        else :
            merged_list.append(list2[0])
            list2.remove(list2[0])

    if len(list1) == 0 :
        merged_list += list2
    else :
         merged_list += list1
    
    return merged_list

def merge_sort(unsorted_list):
    if len(unsorted_list) == 0 or len(unsorted_list) == 1 :
        return unsorted_list
    else:
        mid = int(len(unsorted_list)/2)
        list1 = merge_sort(unsorted_list[:mid])
        list2 = merge_sort(unsorted_list[mid:])
        return merge(list1,list2)

if __name__ == "__main__":
    input_list = [99,88,77,55,44,22,11,1]
    sorted_list = merge_sort(input_list)
    print(sorted_list)
