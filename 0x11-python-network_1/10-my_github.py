#!/usr/bin/python3
""" Module containing script using requests and sys to access GitHub API
"""

import requests
import sys


if __name__ == "__main__":
    auth = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=auth)
    print('{}'.format(r.json().get('id')))
