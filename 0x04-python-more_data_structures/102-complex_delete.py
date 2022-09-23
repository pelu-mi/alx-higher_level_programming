#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None or a_dictionary == []:
        return a_dictionary
    for item in sorted(a_dictionary):
        if a_dictionary[item] == value:
            del(a_dictionary[item])
    return a_dictionary
