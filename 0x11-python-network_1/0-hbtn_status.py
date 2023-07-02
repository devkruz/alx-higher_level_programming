#!/usr/bin/python3
# Fetche https://alx-intranet.hbtn.io/status
import urllib.request as request

if __name__ == '__main__':
    with request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        respond = resp.read()
        print("Body response:\n- type: {}\n- content: {}\n- utf8 content: {}"
              .format((type(respond)), respond, respond.decode("utf-8")))
