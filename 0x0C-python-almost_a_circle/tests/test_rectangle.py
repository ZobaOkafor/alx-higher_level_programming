#!/usr/bin/env python3
"""
Unit tests for Rectangle class
"""

import unittest
import io
import sys
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def test_rectangle_creation(self):
        """Test creating a Rectangle"""
        r1 = Rectangle(5, 10)
        self.assertIsInstance(r1, Rectangle)
        self.assertIsInstance(r1, Base)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertNotEqual(r1.id, None)

    def test_rectangle_attributes(self):
        """Test setting attributes of a Rectangle"""
        r2 = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 3)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 5)
        self.assertEqual(r2.id, 6)

    def test_rectangle_area(self):
        """Test calculating the area of a Rectangle"""
        r3 = Rectangle(4, 5)
        self.assertEqual(r3.area(), 20)

    def test_rectangle_display(self):
        """Test displaying a Rectangle"""
        r4 = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with unittest.mock.patch(
                'sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r4.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_rectangle_str(self):
        """Test the string representation of a Rectangle"""
        r5 = Rectangle(3, 4, 5, 6, 7)
        expected_str = "[Rectangle] (7) 5/6 - 3/4"
        self.assertEqual(str(r5), expected_str)

    def test_rectangle_update_args(self):
        """Test updating a Rectangle with args"""
        r6 = Rectangle(1, 1)
        r6.update(10, 2, 3, 4, 5)
        self.assertEqual(r6.id, 10)
        self.assertEqual(r6.width, 2)
        self.assertEqual(r6.height, 3)
        self.assertEqual(r6.x, 4)
        self.assertEqual(r6.y, 5)

    def test_rectangle_update_kwargs(self):
        """Test updating a Rectangle with kwargs"""
        r7 = Rectangle(7, 8)
        r7.update(id=20, x=5, y=6)
        self.assertEqual(r7.id, 20)
        self.assertEqual(r7.width, 7)
        self.assertEqual(r7.height, 8)
        self.assertEqual(r7.x, 5)
        self.assertEqual(r7.y, 6)

    def test_rectangle_to_dictionary(self):
        """Test converting Rectangle to dictionary"""
        r8 = Rectangle(3, 4, 5, 6, 7)
        expected_dict = {'id': 7, 'width': 3, 'height': 4, 'x': 5, 'y': 6}
        self.assertEqual(r8.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
