"""
Write a function that determines whether or not the given number(argument) is prime.

"""


def is_prime(num):

    for  i in range(2,int((num*(1/2)))+1):
        
        if num%i == 0:

            return "the number is not prime."
    
    return "the number is prime."

result = is_prime(4567)
print(result)#the number is prime.


"""
Written function is based on the following Theorem;

Let p be an integer greater than 1,then,

(p is not prime) if and only if (There exits a quotient d such that d|p and 2=<d=<squared(p)) 
"""

