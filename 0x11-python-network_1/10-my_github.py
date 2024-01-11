#!/usr/bin/python3
"""this module is doing something"""
import requests
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]

    url = "https://api.github.com/user"

    r = requests.get(url, auth=(username, password))

    if r.status_code == 200:
        data = response.json()
        print(data.get('id'))
    else:
        print('None')
