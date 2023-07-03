#!/usr/bin/python3
"""
Sends a POST request to the passed URL with
the email as a parameter,
and finally displays the body of the response.
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    respond = requests.get(url)
    if respond.status_code >= 400:
        print("Error code: {}".format(respond.status_code))
    else:
        print(respond.text)
