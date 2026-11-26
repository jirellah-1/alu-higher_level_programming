#!/usr/bin/python3
"""Module that adds two numbers.

This module defines the function add_integer, which adds two integers
or floats and returns the result as an integer.
"""


def add_integer(a, b=98):
    """Add two integers and return the result.

    Floats are casted to integers before the addition.

    Args:
        a (int or float): the first number.
        b (int or float): the second number (default is 98).

    Returns:
        int: the addition of a and b.

    Raises:
        TypeError: if a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
