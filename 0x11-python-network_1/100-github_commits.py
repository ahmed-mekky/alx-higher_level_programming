#!/usr/bin/python3
"""this module is doing something"""
import requests
from sys import argv

if __name__ == "__main__":
    owner = argv[2]
    repo = argv[1]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    r = requests.get(url)
    json = r.json()
    if r.status_code == 200:
        for i in range(10):
            print(f"{json[i]['sha']}: {json[i]['commit']['author']['name']}")
