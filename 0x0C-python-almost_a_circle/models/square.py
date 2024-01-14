#!/usr/bin/env python3
"""
Square module
"""

from rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor method for Square class.

        Args:
            size (int): Size of the square.
            x (int): x-coordinate of the square.
            y (int): y-coordinate of the square.
            id (int): Identifier for the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter method for size.

        Returns:
            int: Size of the square.
        """
        return (self.width)

    @size.setter
    def size(self, value):
        """
        Setter method for size.

        Args:
            value (int): Size to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update attributes of the Square instance.

        Args:
            *args (ints): List of arguments.
                - 1st argument represents id attribute.
                - 2nd argument represents size attribute.
                - 3rd argument represents x attribute.
                - 4th argument represents y attribute.
            **kwargs (dict): Dictionary of keyworded arguments.
        """

        if args:
            attr_list = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attr_list[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
        """

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: String representation of the square.
        """
        return ("[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
        ))

    def to_dictionary(self):
        """
        Return the dictionary representation of the square.

        Returns:
            dict: Dictionary representation of the square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
