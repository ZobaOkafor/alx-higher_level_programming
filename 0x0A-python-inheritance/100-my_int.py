#!/usr/bin/python3
"""Defines a MyInt class that inherits from int"""


class MyInt(int):
    """Represent a rebel integer"""

    def __eq__(self, other):
        """Override the equality operator =="""
        return (super().__ne__(other))

    def __ne__(self, other):
        """Override the inequality operator !="""
        return (super().__eq__(other))
