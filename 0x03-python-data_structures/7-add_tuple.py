#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    if len(a) < 2:
        if len(a) == 0:
            a.append(0)
        a.append(0)
    if len(b) < 2:
        if len(b) == 0:
            b.append(0)
        b.append(0)
    num1 = a[0] + b[0]
    num2 = a[1] + b[1]
    new_tuple = (num1, num2)
    return new_tuple
