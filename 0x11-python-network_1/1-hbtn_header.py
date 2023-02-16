#!/usr/bin/python3
""" Module containing script using urllib and sys
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in
the header of the response.
"""

from urllib import request
import sys


req = request.Request(sys.argv[1])
with request.urlopen(req) as response:
    res = response.info()
    print('{}'.format(res['X-Request-Id']))
