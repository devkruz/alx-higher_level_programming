#!/usr/bin/python3
"""
Sends a POST request to the passed URL with
the email as a parameter,
and finally displays the body of the response.
"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    url = "https://api.github.com/user"
    res = requests.get(url, auth=auth)
    print(res.json().get("id"))
