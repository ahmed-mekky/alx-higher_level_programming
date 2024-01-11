#!/usr/bin/python3
from urllib import request
"""this module is doing something"""

with request.urlopen("https://alx-intranet.hbtn.io/status") as r:
    b_content = r.read()
    print(f"""Body response:
    - type: {type(b_content)}
    - content: {b_content}
    - utf8 content: {b_content.decode("UTF-8")}""")
