#!/usr/bin/python3
def roman_to_int(roman_string):
    if not (isinstance(roman_string, str)) or roman_string is None:
        return 0
    num = 0
    prev = ''
    for i in roman_string:
        if i == 'M':
            num += 1000
        if i == 'D':
            if prev == 'C':
                num += 300
            else:
                num += 500
        if i == 'C':
            if prev == 'X':
                num += 80
            else:
                num += 100
        if i == 'L':
            if prev == 'X':
                num += 30
            else:
                num += 50
        if i == 'X':
            if prev == 'I':
                num += 8
            else:
                num += 10
        if i == 'V':
            if prev == 'I':
                num += 3
            else:
                num += 5
        if i == 'I':
            num += 1

        prev = i
    return num
