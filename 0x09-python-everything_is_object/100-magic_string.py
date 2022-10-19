#!/usr/bin/python
def magic_string(n=0):
    magic_string.count = getattr(magic_string, 'count', 0) + 1
    return ("BestSchool, " * (magic_string.count - 1) + "BestSchool")
