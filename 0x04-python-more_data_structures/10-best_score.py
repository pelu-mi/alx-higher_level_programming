#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary != None:
        new_list = [a_dictionary[x] for x in sorted(a_dictionary)]
        return max(new_list)
    else:
        return None
