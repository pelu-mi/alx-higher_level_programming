#!/usr/bin/python3
"""Module containing script using urllib and sys
"""

from urllib import request, parse, error.HTTPError
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    req = request.Request(url, data)
    try:
        with request.urlopen(req) as response:
            res = response.read()
            print(res.decode('utf-8'))
    except error.HTTPError as e:
        print('Error Code: {}'.format(e.code)
