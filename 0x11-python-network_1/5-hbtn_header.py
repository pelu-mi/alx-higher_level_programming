#!/usr/bin/python3
""" Module containing script using requests and sys
"""

import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print('{}'.format(r.headers.get('X-Request-Id')))
