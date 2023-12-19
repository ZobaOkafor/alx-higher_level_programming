#!/usr/bin/python3

"""Module for defining the Square class"""


class Square:
    """
    A class that defines a square.

    Attributes:
        __size (float or int): The size of the square.

    Methods:
        size() -> float or int: Retrieve the size of the square.
        size(value) -> None: Set the size of the square.
        area() -> float or int: Calculate the area of the square.
        __eq__(other) -> bool: Compare two squares for equality
        based on area.
        __ne__(other) -> bool: Compare two squares for inequality
        based on area.
        __lt__(other) -> bool: Compare if one square is less than
        another based on area.
        __le__(other) -> bool: Compare if one square is less than
        or equal to another based on area.
        __gt__(other) -> bool: Compare if one square is greater than
        another based on area.
        __ge__(other) -> bool: Compare if one square is greater than
        or equal to another based on area.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (float or int, optional): The size of the square.
            Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (float or int): The new size for the square.

        Raises:
            TypeError: If size is not a number (float or int).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return (self.__size ** 2)

    def __eq__(self, other):
        """
        Compare two squares for equality based on area.

        Args:
            other (Square): The square to compare against.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        return (self.area() == other.area())

    def __ne__(self, other):
        """
        Compare two squares for inequality based on area.

        Args:
            other (Square): The square to compare against.

        Returns:
            bool: True if areas are not equal, False otherwise.
        """
        return (self.area() != other.area())

    def __lt__(self, other):
        """
        Compare if one square is less than another based on area.

        Args:
            other (Square): The square to compare against.

        Returns:
            bool: True if area is less than the other square, False otherwise.
        """
        return (self.area() < other.area())

    def __le__(self, other):
        """
        Compare if one square is less than or equal to another
        based on area.

        Args:
            other (Square): The square to compare against.

        Returns:
            bool: True if area is less than or equal to the other
            square, False otherwise.
        """
        return (self.area() <= other.area())

    def __gt__(self, other):
        """
        Compare if one square is greater than another based on area.

        Args:
            other (Square): The square to compare against.

        Returns:
            bool: True if area is greater than the other square,
            False otherwise.
        """
        return (self.area() > other.area())

    def __ge__(self, other):
        """
        Compare if one square is greater than or equal to another
        based on area.

        Args:
            other (Square): The square to compare against.

        Returns:
            bool: True if area is greater than or equal to the
            other square, False otherwise.
        """
        return (self.area() >= other.area())
