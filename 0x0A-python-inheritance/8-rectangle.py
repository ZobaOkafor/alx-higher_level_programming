#!/usr/bin/python3

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
