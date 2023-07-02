#!/usr/bin/python3
""" ends a request to the URL and displays the body of the response """

import urllib.request as request
import urllib.error as error
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with request.urlopen(url) as resp:
            print(resp.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code:", e.code)
