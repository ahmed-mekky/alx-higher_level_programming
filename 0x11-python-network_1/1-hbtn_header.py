#!/usr/bin/python3
from urllib import request
from sys import argv
"""this module is doing something"""

with request.urlopen(argv[1]) as r:
    headers = r.headers
    print(headers.get('X-Request-Id'))
