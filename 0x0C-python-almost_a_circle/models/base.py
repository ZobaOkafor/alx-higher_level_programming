#!/usr/bin/python3
"""Base module"""


import json
import csv
import os
import turtle


class Base:
    """
    Base class for managing id attribute

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor method for Base class

        Args:
            id (int): The identity of the new Base.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None:
                file.write(cls.to_json_String([]))
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by json_string

         Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        return (json.loads(json_string) if json_string else [])

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set using a dictionary.

        Args:
            dictionary (dict): Dictionary of attributes.

        Returns:
            Base: Instance with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()
        dummy_instance.update(**dictionary)
        return (dummy_instance)

    @classmethod
    def load_from_file(cls):
        """
        Load a list of instances from a file.

        Returns:
            List: List of instances.
        """
        filename = cls.__name__ + ".json"
        instances = []
        if os.path.isfile(filename):
            with open(filename, mode="r", encoding="utf-8") as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                instances = [cls.create(**d) for d in list_dicts]
        return (instances)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save a list of instances to a file in CSV format.

        Args:
            list_objs (list): List of instances.

        Returns:
            None
        """
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if list_objs is not None:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow([obj.id, obj.width,
                                        obj.height, obj.x, obj.y])
                    elif cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Load a list of instances from a file in CSV format.

        Returns:
            list: List of instances.
        """
        filename = cls.__name__ + ".csv"
        instances = []
        if os.path.isfile(filename):
            with open(
                filename, mode="r", newline="", encoding="utf-8"
            ) as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        dict_data = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])
                        }
                    elif cls.__name__ == "Square":
                        dict_data = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                        }
                    instances.append(cls.create(**dict_data))
        return (instances)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draw Rectangles and Squares using Turtle graphics """
        turtle.speed(2)
        turtle.bgcolor("white")
        turtle.title("Rectangles and Squares")

        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)
            turtle.left(90)
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)
            turtle.left(90)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)

        turtle.done()
