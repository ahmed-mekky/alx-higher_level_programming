#!/usr/bin/python3
"""this module is doing something"""
import requests
from sys import argv

if __name__ == "__main__":
    data = {"q": argv[1] if len(argv) == 2 else ""}
    r = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        r_json = r.json()
        if not r_json:
            print("No result")
        else:
            print(f"[{r_json.get('id')}] {r_json.get('name')}")
    except ValueError:
        print("Not a valid JSON")
