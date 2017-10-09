def getPower(base, exponent):
    return _getPower(base, exponent) if (exponent >= 0) else 1. / _getPower(base, exponent * -1);

def _getPower(base, exponent):
    """
    Given 2 numbers x and y, this function computes x raised to the power of y.
    this is a divide and conquer algorithm which means that this function does
    not multiply x times itself y times, it takes into consideration that if y is
    an even number then x^y = x^(y/2) * x^(y/2). If y is an odd number then
    x^y = x^((y-1) / 2) * x^((y-1) / 2) * x. This of course saves a lot of work.
    this algorithm runs in O(log y) instead of O(y)
    """
    # The exponent is 0 so the answer is 1
    if (exponent == 0):
        return 1;

    # The exponent is even so base ^ exponent = base ^ (exponent / 2) * base ^ (exponent / 2)
    if (exponent % 2 == 0):
        root = _getPower(base, exponent / 2);
        return root * root;

    # The exponent is not even so base ^ exponent = base ^ ((exponent - 1) / 2) * base ^ ((exponent - 1) / 2)
    semiRoot = _getPower(base, (exponent - 1) / 2); # Sorry for that silly name but could not find a better one :)
    return semiRoot * semiRoot * base;

while(True):
    try:
        base = input("Enter the base: ");
        exponent = input("Enter the exponent: ");

        result = getPower(base, exponent);
        print("{0} ^ {1} = {2}".format(base, exponent, result));
        break;

    except Exception as e:
        print("------------------------------------------------")
        print("Please Enter both a base and an integer exponent");
