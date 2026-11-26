#!/usr/bin/python3
"""Module that prints a text with indentation.

This module defines the function text_indentation, which prints a text
with 2 new lines after each of the characters . ? and :
"""


def text_indentation(text):
    """Print a text with 2 new lines after each . ? and : character.

    Spaces at the beginning and at the end of each printed line are removed.

    Args:
        text (str): the text to print.

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    skip = False
    for char in text:
        if skip and char == " ":
            continue
        skip = False
        result += char
        if char in ".?:":
            result += "\n\n"
            skip = True
    print(result.strip(" "), end="")
