#!/usr/bin/python3
"""Program to solve the N queens problem
Place N non-attacking queens on an NxN chessboard
"""


import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    n = int(sys.argv[1])
except Exception as e:
    print("N must be a number")
    exit(1)


if not isinstance(n, int):
    print("N must be a number")
    exit(1)
if n < 4:
    print("N must be at least 4")
    exit(1)


