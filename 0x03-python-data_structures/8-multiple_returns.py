#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = ""
    if sentence != "":
        first = sentence[0]
    else:
        first = None
    return length, first
