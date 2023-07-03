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
    email = sys.argv[2]
    data = {"email": email}
    respond = requests.post(url, data=data)
    print(respond.text)
