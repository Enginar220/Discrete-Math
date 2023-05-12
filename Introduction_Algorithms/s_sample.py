

def st_sample(samp):

    # type(samp)==list

    sum_samp = 0
    
    for i in samp:
        sum_samp += i
    
    mean_samp = sum_samp/len(samp)

    result = 0

    for j in samp:

        result += (j-mean_samp)**2
    
    result = (result/(len(samp)-1))**(1/2)

    return result


example = [4.8,2.1,0.4,12.3,0.1,3,-2.8,4.3,5.9,7.3]

ex = st_sample(example)

print(ex)