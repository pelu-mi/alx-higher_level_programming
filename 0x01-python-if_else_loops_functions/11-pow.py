#!/usr/bin/python3
def pow(a, b):
    if b = 0:
        return 1
    if b > 0:
        i = 0
        prod = 1
        while i < b:
            prod = prod * a
            i += 1
        return prod
    if b < 0:
        return abs(a ** b)
