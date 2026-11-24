#!/usr/bin/python3
"""Script that displays the X-Request-Id header of a response."""
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.info().get("X-Request-Id"))
