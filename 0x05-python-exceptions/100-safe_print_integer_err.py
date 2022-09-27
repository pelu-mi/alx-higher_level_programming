#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    res = False
    try:
        print("{:d}".format(value))
        res = True
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
    return res
