#!/usr/bin/python3
"""Module that defines a Rectangle class that counts its instances."""


class Rectangle:
    """Defines a rectangle by its private, validated width and height.

    Attributes:
        number_of_instances (int): the number of Rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): the width of the rectangle (default is 0).
            height (int): the height of the rectangle (default is 0).
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width after validating it.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height after validating it.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle, or 0 if a side is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the rectangle drawn with #, or an empty string."""
        if self.__width == 0 or self.__height == 0:
            return ""
        row = "#" * self.__width
        return "\n".join([row] * self.__height)

    def __repr__(self):
        """Return a string that eval() can use to recreate the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message and update the count when a rectangle is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
