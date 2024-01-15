#!/usr/bin/env python3
"""Unit tests for Base class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import io
import sys
import os


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def setUp(self):
        """Reset the Base class's _nb_objects counter before each test"""
        Base._Base__nb_objects = 0

    def test_base_incrementing_ids(self):
        """Test if ids are incremented correctly"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_base_custom_id(self):
        """Test if custom id is assigned correctly"""
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_base_mixed_ids(self):
        """Test if mixed ids are handled correctly"""
        b5 = Base()
        b6 = Base(15)
        b7 = Base()
        # Since three instances were created before with ids 1, 2, and 3
        self.assertEqual(b5.id, 4)
        self.assertEqual(b6.id, 15)
        # Incremented from the last instance
        self.assertEqual(b7.id, 5)

    def test_base_to_json_string_empty(self):
        """Test if to_json_string returns an empty list representation
        for an empty list"""
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_base_to_json_string_none(self):
        """Test if to_json_string returns an empty list representation
        for None"""
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_base_to_json_string(self):
        """Test if to_json_string returns the correct JSON string
        representation"""
        b8 = Base(10)
        b9 = Base(20)
        result = Base.to_json_string([
            b8.to_dictionary(),
            b9.to_dictionary()
        ])
        expected = '[{"id": 10}, {"id": 20}]'
        self.assertEqual(result, expected)

    def test_base_from_json_string_empty(self):
        """Test if from_json_string returns an empty list for an
        empty JSON string"""
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

    def test_base_from_json_string_none(self):
        """Test if from_json_string returns an empty list for None"""
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_base_from_json_string(self):
        """Test if from_json_string returns the correct list
        representation"""
        json_string = '[{"id": 5}, {"id": 15}]'
        result = Base.from_json_string(json_string)
        expected = [{"id": 5}, {"id": 15}]
        self.assertEqual(result, expected)

    def test_base_create(self):
        """Test if create returns an instance with attributes
        set from dictionary"""
        dictionary = {"id": 1, "width": 5, "height": 10}
        result = Base.create(**dictionary)
        self.assertIsInstance(result, Base)
        self.assertEqual(result.id, 1)
        self.assertEqual(result.width, 5)
        self.assertEqual(result.height, 10)

    def test_base_draw(self):
        """Test if draw method opens a window and draws all the
        Rectangles and Squares"""
        # Create StringIO object to capture output
        captured_output = io.StringIO()
        sys.stdout = captured_output  # Redirect stdout
        list_rectangles = [
            Rectangle(100, 40),
            Rectangle(90, 110, 30, 10),
            Rectangle(20, 25, 110, 80)
        ]
        list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]
        Base.draw(list_rectangles, list_squares)
        sys.stdout = sys.__stdout__  # Reset redirect.
        # Assert that something was printed
        self.assertNotEqual(captured_output.getvalue(), "")


if __name__ == '__main__':
    unittest.main()
