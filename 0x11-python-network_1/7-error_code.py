#!/usr/bin/python3
""" Module containing script using requests and sys
"""

import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if (r.status_code != requests.codes.ok):
        print('Error code: {}'.format(r.status_code))
    else:
        print(r.text)
