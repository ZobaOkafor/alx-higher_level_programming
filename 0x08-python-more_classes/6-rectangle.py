#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """
    Rectangle class

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        number_of_instances (int): Number of instances of Rectangle.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with optional width and height.

        Args:
            width (int): Width of the rectangle. Default is 0.
            height (int): Height of the rectangle. Default is 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
            int: Width of the rectangle.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value (int): New value for the width attribute.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
            int: Height of the rectangle.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): New value for the height attribute.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Computes and returns the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Computes and returns the perimeter of the rectangle.

        Returns:
            int: Perimeter of the rectangle.
        """
        return (2 * (self.__width + self.__height)
                if self.__width and self.__height else 0)

        def __str__(self):
            """
        Returns a string representation of the rectangle.

        Returns:
            str: String representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        return ("\n".join(['#' * self.__width for _ in range(self.__height)]))

    def __repr__(self):
        """
        Returns a string representation of the rectangle for recreation.

        Returns:
            str: String representation of the rectangle.
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted and
        decrements the number_of_instances attribute.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
