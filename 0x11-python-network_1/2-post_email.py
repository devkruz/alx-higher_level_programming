#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter """

import urllib.request as request
import urllib.parse as parse
import sys
if __name__ == '__main__':
    url_value = parse.urlencode({'Email': sys.argv[2]})
    print(url_value)
    full_url = sys.argv[1] + '?' + url_value
    print(full_url)
    with request.urlopen(full_url) as resp:
        print(resp.read().decode("utf-8"))
