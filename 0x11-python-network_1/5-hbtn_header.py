#!/usr/bin/python3
"""
Sends a request to the URL and displays the
value of the variable X-Request-Id in the response header
 """

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    respond = requests.get(url)
    print(respond.headers.get("X-Request-Id"))
