#!/usr/bin/python3
from urllib import request, parse
from sys import argv
"""this module is doing something"""

url = argv[1]
data = {"email": argv[2]}
data = urllib.parse.urlencode(data).encode()
req = urllib.request.Request(url, data=data)

with urllib.request.urlopen(req) as r:
    print(r.read().decode("UTF-8"))

