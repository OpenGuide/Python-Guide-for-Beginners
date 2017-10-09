def linearSearch(item, list):
    found = False
    position = 0

    while position < len(list) and not found:
        if list[position] == item:
            found = True
        position = position + 1
    return found


if __name__ == "__main__":
    itemList = ["apple", "banana", "cocoa", "durian"]
    input = input("what item do you want to find?")
    isItFound = linearSearch(input, itemList)
    if isItFound:
        print("your item is in the list!")
    else:
        print("your item is not in the list!")
