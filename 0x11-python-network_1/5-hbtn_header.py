#!/usr/bin/python3
""" Fetch https://alx-intranet.hbtn.io/status """

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    respond = requests.get(url)
    print(respond.headers.get("X-Request-Id"))
