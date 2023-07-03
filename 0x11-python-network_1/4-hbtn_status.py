#!/usr/bin/python3
""" Fetch https://alx-intranet.hbtn.io/status """

import requests

if __name__ == '__main__':
    respond = requests.get('https://alx-intranet.hbtn.io/status')
    type = "\n\t- type: {}".format(type(respond.text))
    content = "\n\t- content: {}".format(respond.text)
    msg = "Body response:" + type + content
    print(msg)
