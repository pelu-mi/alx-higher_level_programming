#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_list = sorted(a_dictionary)
    for i in range(len(dict_list)):
        print("{}: {}".format(dict_list[i], a_dictionary[dict_list[i]]))
