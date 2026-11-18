#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an area method."""


class BaseGeometry:
    """A base class for geometry shapes with an unimplemented area."""

    def area(self):
        """Raise an exception because area is not implemented yet."""
        raise Exception("area() is not implemented")
