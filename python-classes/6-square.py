#!/usr/bin/python3
"""Module that defines a Square class with a size and a position."""


class Square:
    """Defines a square with a validated size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): the size of the square (default is 0).
            position (tuple): the offset of the square when printed
                (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after validating it.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position after validating it.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(type(i) is int for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with # at its position, or an empty line."""
        if self.__size == 0:
            print()
            return
        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
