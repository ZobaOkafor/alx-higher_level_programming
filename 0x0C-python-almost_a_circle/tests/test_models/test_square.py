#!/usr/bin/python3
""" 13-main """

import io
import sys
from models.base import Base
from models.square import Square
import unittest


class TestSquare(unittest.TestCase):
    """
    Test cases for Square class
    """

    def test_square_attributes(self):
        """
        Test if Square attributes are initialized correctly
        """
        s = Square(10, 20, 30, 1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 20)
        self.assertEqual(s.y, 30)
        self.assertEqual(s.id, 1)

    def test_invalid_size(self):
        """
        Test if TypeError and ValueError are raised for invalid size
        """
        with self.assertRaises(TypeError):
            s = Square(-5)
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_invalid_x(self):
        """
        Test if TypeError and ValueError are raised for invalid x-coordinate
        """
        with self.assertRaises(TypeError):
            s = Square(5, "invalid_x")
        with self.assertRaises(ValueError):
            s = Square(5, -1)

    def test_invalid_y(self):
        """
        Test if TypeError and ValueError are raised for invalid y-coordinate
        """
        with self.assertRaises(TypeError):
            s = Square(5, 10, "invalid_y")
        with self.assertRaises(ValueError):
            s = Square(5, 10, -1)

    def test_area(self):
        """
        Test if area is calculated correctly
        """
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_str_representation(self):
        """
        Test if str representation is correct
        """
        s = Square(5, 2, 3, 1)
        self.assertEqual(str(s), "[Square] (1) 2/3 - 5")

    def test_update_method(self):
        """
        Test if update method works correctly
        """
        s = Square(5, 2, 3, 1)
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 2/3 - 5")

        s.update(1, 20)
        self.assertEqual(str(s), "[Square] (1) 2/3 - 20")

        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

        s.update(1, 2, 3, 4, 5)
        self.assertEqual(str(s), "[Square] (1) 4/5 - 2")

        s.update(x=12)
        self.assertEqual(str(s), "[Square] (1) 12/5 - 2")

        s.update(size=7, y=1)
        self.assertEqual(str(s), "[Square] (1) 12/1 - 7")

        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 12/1 - 7")

    def test_to_dictionary_method(self):
        """
        Test if to_dictionary method works correctly
        """
        s = Square(10, 2, 1, 3)
        s_dict = s.to_dictionary()
        self.assertEqual(s_dict, {'id': 3, 'size': 10, 'x': 2, 'y': 1})


if __name__ == '__main__':
    unittest.main()
