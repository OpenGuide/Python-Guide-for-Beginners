# Gets the sum of two numbers after validating user input.

def get_user_input(prompt):
    """
    Prompts the user to type in a decimal number. If the input is invalid, prompts again.
    """
    while True:
        try:
            # input prints the prompt, then waits for the user to type in input.
            # float(...) converts the string to a decimal number. If the input isn't a number, it throws an exception.
            return float(input(prompt))
        except:
            # The input wasn't valid, so we pass and allow the loop to go again.
            pass

if __name__=="__main__":
    x = get_user_input("Please input first number: ")
    y = get_user_input("Please input second number: ")
    sum = x + y

    print("The sum of", x, "and", y, "is", sum)

