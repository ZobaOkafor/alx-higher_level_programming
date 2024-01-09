#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class BaseGeometry:
    """Empty class definition for BaseGeometry."""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value.

        Args:
        - name: a string representing the name
        - value: an integer value to be validated

        Raises:
        - TypeError: if value is not an integer
        - ValueError: if value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class definition for Rectangle, inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Instantiates a Rectangle object with given width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the rectangle description in the specified format."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Class definition for Square, inheriting from Rectangle."""

    def __init__(self, size):
        """Instantiates a Square object with given size."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Returns the square description in the specified format."""
        return ("[Square] {}/{}"
                .format(self._Rectangle__width, self._Rectangle__height))
