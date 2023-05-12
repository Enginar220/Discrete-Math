
def gcd(num1,num2):
    """
    returns the greatest common divisor of the given two numbers

    Args:
    
    num1,num2: Two integers that we will find the greatest common divisor of.

    Returns:

    The greatest common divisor of the given two numbers.
    
    """

    if (num1%num2 == 0):
        print(num2)
    elif (num2%num1 == 0):
        print(num1)
    else:
        c = max(num1,num2)
        d = min(num1,num2)

    