def is_palindrome(num):
    '''
    checks if a number is a palindrome by casting it to a string
    and comparing the first half with the reversed second half
    
    returns True if num is a palindrome, otherwise returns False
    '''
    if type(num) != str:
        num = str(num)
    nlen = int(len(num))
    if nlen % 2 == 0:
        half = int(nlen/2)
        if num[half:] == num[:half][::-1]:
            return True
    else:
        half = int(nlen/2) + 1
        if num[half:] == num[:half-1][::-1]:
            return True
    return False
    
if __name__ == '__main__':
    test = ['1', '22', '121', '1221', '1231']
    for i in test:
        print(is_palindrome(i))