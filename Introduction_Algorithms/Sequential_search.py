


def f(n,t):

    """
    Arguments:
    n = list of elements of types of str or int/float
    t = the element that we are looking for in n.
    
    """
    
    i = 0
    
    while t != n[i]:
        i += 1
    if i == len(n) + 1:
        print(f"Element {t} was not found.")
    else:
        print(f"Element {t} was found in location {i}")


my_list = [1,2,3,4,12,5,"k",6,7,12]

f(my_list,"k")#Element k was found in location 6