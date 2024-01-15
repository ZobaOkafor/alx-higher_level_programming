#!/usr/bin/python3
"""
Rectangle module
"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class, inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor method for Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): x-coordinate of the rectangle.
            y (int): y-coordinate of the rectangle.
            id (int): Identifier for the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method for width.

        Returns:
            int: Width of the rectangle.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Setter method for width.

        Args:
            value (int): Width to set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height.

        Returns:
            int: Height of the rectangle.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Setter method for height.

        Args:
            value (int): Height to set.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter method for x.

        Returns:
            int: x-coordinate of the rectangle.
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Setter method for x.

        Args:
            value (int): x-coordinate to set.

        Raises:
            TypeError: If x is not an integer.
            ValueError: If x is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter method for y.

        Returns:
            int: y-coordinate of the rectangle.
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        Setter method for y.

        Args:
            value (int): y-coordinate to set.

        Raises:
            TypeError: If y is not an integer.
            ValueError: If y is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Print the rectangle using '#' characters to stdout.
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: String representation of the rectangle.
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height
            ))

    def update(self, *args, **kwargs):
        """
        Update attributes of the rectangle.

        Args:
            args (int): Arguments in the order id, width, height, x, y.
            kwargs (dict): Key-worded arguments to update attributes.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                """setattr(self, key, value)"""
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """
        Return a dictionary representation of the rectangle.

        Returns:
            dict: Dictionary representation of the rectangle.
        """
        return {
                'id': self.id,
                'width': self.__width,
                'height': self.__height,
                'x': self.__x,
                'y': self.__y
        }
