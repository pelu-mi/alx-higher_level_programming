#!/usr/bin/python3
""" Module containing script using requests and sys
"""

import requests
import sys


if __name__ == "__main__":
    try:
        q = sys.argv[1]
    except IndexError:
        q = ""
    data_sent = {'q': q}
    r = requests.post('http://0.0.0.0:5000/search_user', data=data_sent)
    try:
        info = r.json()
        if info == {}:
            print('No result')
        else:
            print('[{}] {}'.format(info.get('id'), info.get('name')))
    except ValueError:
        print('Not a valid JSON')
