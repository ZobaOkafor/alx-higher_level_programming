#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square, inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a new square instance

        Args:
            size (int): The size of the square (width and height)
        """
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the square"""
        return ("[Square] {}/{}"
                .format(self._Rectangle__width, self._Rectangle__height))
