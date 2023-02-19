#!/usr/bin/python3
""" Module containing script using requests and sys to access GitHub API
"""

import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[1], sys.argv[2])
    r = requests.get(url)
    commits = r.json()
    i = 0
    for commit in commits:
        print("{}: {}".format(commit.get('sha'), commit.get('commit').get('author').get('name')))
        i = i + 1
        if i >= 10:
            break
