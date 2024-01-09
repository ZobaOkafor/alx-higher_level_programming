#!/usr/bin/python3
"""
Module that contains the Student class.
"""


class Student:
    """
    Defines a student by first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
        - first_name (str): The first name of the student.
        - last_name (str): The last name of the student.
        - age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Parameters:
        - attrs (list): A list of attribute names to be retrieved. Default
        is None, meaning all attributes should be retrieved.

        Returns:
        - dict: A dictionary containing the specified attributes of
        the Student instance.
        """
        if attrs is None:
            return (self.__dict__)

        json_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)
        return (json_dict)
