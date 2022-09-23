#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    weight = 0
    num = 0
    for item in my_list:
        weight += item[0] * item[1]
        num += item[1]
    avg = weight / num
    return avg
