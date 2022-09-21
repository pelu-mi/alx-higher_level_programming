#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = []
    [uniq.append(x) for x in my_list if x not in uniq]
    n = sum(uniq)
    return n
