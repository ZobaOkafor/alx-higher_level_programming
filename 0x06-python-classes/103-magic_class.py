#!/usr/bin/python3

"""Module for defining the Square class"""


import math


class MagicClass:
    """
    A class that represents a magical circle with radius.

    Attributes:
        __radius (float or int): The radius of the magical circle.

    Methods:
        __init__(self, radius): Initializes a new instance
        of the MagicClass.
        area(self) -> float: Calculates and returns the area of the
        magical circle.
        circumference(self) -> float: Calculates and returns the
        circumference of the magical circle.
    """

    def __init__(self, radius):
        """
        Initializes a new instance of the MagicClass.

        Args:
            radius (float or int): The radius of the magical circle.

        Raises:
            TypeError: If the radius is not a number (float or int).
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the magical circle.

        Returns:
            float: The area of the magical circle.
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """
        Calculates and returns the circumference of the magical circle.

        Returns:
            float: The circumference of the magical circle.
        """
        return (2 * math.pi * self.__radius)
