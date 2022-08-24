#!/usr/bin/python3
def remove_char_at(str, n):
    s = list(str)
    del s[n]
    output = "".join(s)
    return output
