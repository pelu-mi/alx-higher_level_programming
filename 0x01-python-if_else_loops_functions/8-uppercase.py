#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            s = chr(ord(c) - 32)
            c = s
    print("{}".format(str))
