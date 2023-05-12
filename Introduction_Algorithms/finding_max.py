#Finding max of a list of numbers

def max_find(given_list):

    max_num = given_list[0] 
    for i in range(1,len(given_list)):
        if given_list[i] > max_num:
            max_num = given_list[i]

    return max_num

x = [51,12,321,3,0,12,12,123]

result = max_find(x)
print(result)
#output:321

