#!/usr/bin/python3
"""this module is doing something"""
from urllib import request, parse
from sys import argv

url = argv[1]
data = {"email": argv[2]}
data = urllib.parse.urlencode(data).encode()
req = urllib.request.Request(url, data=data)

with request.urlopen(req) as r:
    print(r.read().decode("UTF-8"))

