

def fac(num):

    if num == 0:
        return 1
    
    return num * fac(num-1)


result = fac(6)
print(result)#720

