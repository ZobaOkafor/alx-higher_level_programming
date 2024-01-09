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

        args:
        - first_name (str): The first name of the student.
        - last_name (str): The last name of the student.
        - age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
        - dict: A dictionary containing the attributes of the Student instance.
        """
        json_dict = {}
        for key, value in self.__dict__.items():
            json_dict[key] = value
        return (json_dict)
