#!/usr/bin/python3
"""Script that searches a user by letter with a POST request."""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post(url, data={"q": letter})
    try:
        data = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
