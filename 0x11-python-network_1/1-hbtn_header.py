#!/usr/bin/python3
""" Module containing script using urllib and sys
"""

from urllib import request
import sys


req = request.Request(sys.argv[1])
with request.urlopen(req) as response:
    res = response.info()
    print('{}'.format(res['X-Request-Id']))
