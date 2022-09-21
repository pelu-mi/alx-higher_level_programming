#!/usr/bin/python3
def search_replace(my_list, search, replace):
    s_r = list(map(lambda x: replace if x == search else x, my_list))
    return s_r
