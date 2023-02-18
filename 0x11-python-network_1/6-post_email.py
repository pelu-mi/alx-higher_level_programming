#!/usr/bin/python3
""" Module containing script using requests and sys
"""

import requests
import sys


if __name__ == "__main__":
    header_dict = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=header_dict)
    print('Your email is: {}'.format(r.headers.get('email')))
