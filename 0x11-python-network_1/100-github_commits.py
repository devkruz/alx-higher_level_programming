#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""

import sys
import requests

if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits"\
        .format(sys.argv[2], sys.argv[1])
    req = requests.get(url)
    commits = req.json()

    try:
        for index in range(10):
            sha = commits[index].get("sha")
            name = commits[index].get("commit").get("author").get("name")
            print("{}: {}".format(sha, name))
    except IndexError:
        pass
