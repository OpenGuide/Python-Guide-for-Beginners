def for_loop_addition(a,b):
    '''
    Add two numbers in strange way
    '''
    result = 0

    for i in range(a):
        result += 1

    for j in range(b):
        result += 1

    return result

assert for_loop_addition(1,2) ==  1 + 2
assert for_loop_addition(-1,2) == -1 + 2
