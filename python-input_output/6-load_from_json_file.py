#!/usr/bin/python3
"""Module that defines a function to load an object of a JSON file."""
import json


def load_from_json_file(filename):
    """Create an object out of the content of a JSON file."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
