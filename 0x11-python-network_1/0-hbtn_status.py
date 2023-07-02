#!/usr/bin/python3
""" Fetch https://alx-intranet.hbtn.io/status """

import urllib.request as request

if __name__ == '__main__':
    with request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        respond = resp.read()
        type = "\n\t- type: {}".format(type(respond))
        content = "\n\t- content: {}".format(respond)
        uft = "\n\t- utf8 content: {}".format(respond.decode("utf-8"))
        msg = "Body response:" + type + content + uft
        print(msg)
