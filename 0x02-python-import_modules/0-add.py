#!/usr/bin/python3
from add_0 import add


def main():
    pass


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    a = 1
    b = 2
    print("{0} + {1} = {2}".format(a, b, add(a, b)))
    main()
