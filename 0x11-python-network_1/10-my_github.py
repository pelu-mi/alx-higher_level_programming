#!/usr/bin/python3
""" Module containing script using requests and sys to access GitHub API
"""

import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    # Start from here

    url = 'https://api.github.com/users/' + sys.argv[1]
    auth = 'Bearer ' + sys.argv[2]
    data_sent = {'Accept': 'application/vnd.github+json',
                 'Authorization': auth,
                 'X-GitHub-Api-Version': '2022-11-28'}
    r = requests.get(url)
    try:
        info = r.json()
        if info.get('message') != 'Bad credentials':
            print('{}'.format(info.get('id')))
        else:
            print('None')
    except ValueError:
        print('None')
