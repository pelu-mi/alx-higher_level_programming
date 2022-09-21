#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        m = ''
        num = -10000
        for i in sorted(a_dictionary):
            if a_dictionary[i] > num:
                num = a_dictionary[i]
                m = i
        return m
    else:
        return None
