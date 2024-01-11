#!/usr/bin/python3
from urllib import request
"""this module is doing something"""

with request.urlopen("https://alx-intranet.hbtn.io/status") as r:
    b_content = r.read()
    print(f"Body response:\n\t- type: {type(b_content)}")
    print(f"\t- content: {b_content}")
    print(f"\t- utf8 content: {b_content.decode('UTF-8')}")
