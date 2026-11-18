#!/usr/bin/python3
"""Module that defines MyList, a list with a sorted printing method."""


class MyList(list):
    """A list subclass that can print itself in ascending order."""

    def print_sorted(self):
        """Print the list in ascending order without changing it."""
        print(sorted(self))
