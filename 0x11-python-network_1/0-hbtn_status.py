#!/usr/bin/python3
""" Module containing script using urllib
"""

from urllib import request


if __name__ == "__main__":
    req = request.Request('https://alx-intranet.hbtn.io/status')
    with request.urlopen(req) as response:
        res = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(res)))
        print('\t- content:', res)
        print('\t- utf8 content:', res.decode())
