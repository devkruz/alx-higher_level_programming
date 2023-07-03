#!/usr/bin/python3
"""
Sends a POST request to the passed URL with
the email as a parameter,
and finally displays the body of the response.
"""

import requests
import sys

if __name__ == '__main__':
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    respond = requests.post(url, data={'q': letter})

    try:
        jres = respond.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if jres == {}:
            print("No result")
        else:
            print("[{}] {}".format(jres.get("id"), jres.get("name")))
