#!/usr/bin/python3
""" Module containing script using requests and sys to access GitHub API
"""

import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    r = requests.get(url)
    commits = r.json()
    i = 0
    for commit in commits:
        name = commit.get('commit').get('author').get('name')
        print("{}: {}".format(commit.get('sha'), name))
        i = i + 1
        if i >= 10:
            break
