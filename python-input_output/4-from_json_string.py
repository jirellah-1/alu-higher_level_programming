#!/usr/bin/python3
"""Module that defines a function to rebuild an object out of JSON."""
import json


def from_json_string(my_str):
    """Return the object represented by a JSON string."""
    return json.loads(my_str)
