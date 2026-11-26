#!/usr/bin/python3
"""Module that defines the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle with size, position and id."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def _check(name, value, strict):
        """Validate value as an int; strict means it must be > 0."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if strict and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if not strict and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width after validating it."""
        self._check("width", value, True)
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height after validating it."""
        self._check("height", value, True)
        self.__height = value

    @property
    def x(self):
        """Get the x offset of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x offset after validating it."""
        self._check("x", value, False)
        self.__x = value

    @property
    def y(self):
        """Get the y offset of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y offset after validating it."""
        self._check("y", value, False)
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle with the character #, using x and y."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assign attributes from args, or from kwargs if no args."""
        attrs = ["id", "width", "height", "x", "y"]
        if args:
            for name, value in zip(attrs, args):
                setattr(self, name, value)
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle."""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
