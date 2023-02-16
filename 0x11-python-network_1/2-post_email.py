#!/usr/bin/python3
"""Module containing script using urllib and sys
"""

from urllib import request, parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    value = {'email': email}

    data = parse.urlencode(value)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        res = response.read()
        print(res.decode('utf-8'))
