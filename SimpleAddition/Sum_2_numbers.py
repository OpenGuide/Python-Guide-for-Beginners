def add_numbers(*args):
    sum = 0
    for arg in args:
        try:
            sum += int(arg)
        except:
            print(">"+arg+"<" + " isnt a valid number")
    print(sum)
