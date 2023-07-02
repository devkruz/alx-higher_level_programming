#!/usr/bin/python3
"""
Displays the value of the `X-Request-Id`
variable found in the header of the response.
"""

import urllib.request as request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    with request.urlopen(url) as resp:
        print(resp.headers["X-Request-Id"])
