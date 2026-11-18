#!/usr/bin/python3
"""Module that defines a function that builds Pascal's triangle."""


def pascal_triangle(n):
    """Return Pascal's triangle of n as a list of lists of integers."""
    if n <= 0:
        return []
    triangle = [[1]]
    for _ in range(n - 1):
        prev = triangle[-1]
        middle = [a + b for a, b in zip(prev, prev[1:])]
        triangle.append([1] + middle + [1])
    return triangle
