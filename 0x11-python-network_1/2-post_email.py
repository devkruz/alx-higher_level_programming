#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter """

import urllib.request as request
import urllib.parse as parse
import sys
if __name__ == '__main__':
    data = parse.urlencode({'email': sys.argv[2]})
    url = sys.argv[1] + '?' + data
    with request.urlopen(url) as resp:
        print(resp.read().decode("utf-8"))
