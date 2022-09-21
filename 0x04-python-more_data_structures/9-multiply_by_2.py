#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {x: a_dictionary[x] * 2 for x in sorted(a_dictionary)}
    return new_dict
