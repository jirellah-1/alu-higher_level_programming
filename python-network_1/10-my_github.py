#!/usr/bin/python3
"""Script that displays the id of a GitHub user using the GitHub API."""
import requests
import sys

if __name__ == "__main__":
    auth = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))
