"""
Write a function that determines whether or not the given number is prime.

"""

def is_prime(num):

    for  i in range(2,int((num*(1/2)))+1):
        
        if num%i == 0:

            return "the number is not prime."
    
    return "the number is prime."

result = is_prime(4567)
print(result)