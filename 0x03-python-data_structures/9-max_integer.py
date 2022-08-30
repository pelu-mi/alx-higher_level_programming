#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    maxVal = 0
    for i in range(len(my_list)):
        if my_list[i] > maxVal:
            maxVal = my_list[i]
    return maxVal
