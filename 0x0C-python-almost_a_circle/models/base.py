#!/usr/bin/python3
""" Module for Base class
"""


import json
import os
import csv
import turtle


class Base:
    """ Class Base
    This class represents the base class of the project.
    It has a class attribute __nb_objects serves as the number of
    class objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize Base class with id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Class Method to convert input to json string

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            str: JSON representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Class method to write json representation of list_objs to a file
        with a filename <class name>.json

        Args:
            list_objs (list): List of instances inheriting from Base
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """ Static method to convert json string to list of objects

        Args:
            json_string (str): Json representation of list of objects

        Returns:
            list: Empty list or list of dictionaries of instances of objects
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Class method to create new instance from dictionary of attributes

        Args:
            dictionary (dict): Dictionary of attributes and values

        Returns:
            obj: Instance of Rectangle or square based on dictionary
        """
        if dictionary is not None and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """ Class method to load class instance from file <class_name>.json

        Returns:
            list: List of instances of class
        """
        filename = cls.__name__ + ".json"
        if not os.path.isfile(filename):
            return []
        instances = []
        # Unpack items in file using from_json_string
        with open(filename, 'r', encoding='utf-8') as f:
            list_dicts = Base.from_json_string(f.read())
            for item in list_dicts:
                instances.append(cls.create(**item))
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Class method to save a list of instances to a csv file
        <class_name>.csv

        Args:
            list_objs (list): List of instances to save
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            if cls.__name__ == "Rectangle":
                # Handle Rectangle
                writer.writerow(["id", "width", "height", "x", "y"])
                for item in list_objs:
                    id = item.id
                    width = item.width
                    height = item.height
                    x = item.x
                    y = item.y
                    writer.writerow([id, width, height, x, y])
            else:
                # Handle Square
                writer.writerow(["id", "size", "x", "y"])
                for item in list_objs:
                    id = item.id
                    size = item.size
                    x = item.x
                    y = item.y
                    writer.writerow([id, size, x, y])

    @classmethod
    def load_from_file_csv(cls):
        """ Class method to load class instance from file <class name>.csv

        Returns:
            list: List of instances of class
        """
        filename = cls.__name__ + ".csv"
        if not os.path.isfile(filename):
            return []
        instances = []
        # Unpack items in file
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            header = next(reader)  # First line is the header
            for row in reader:
                # Handle rectangle
                if cls.__name__ == "Rectangle":
                    # Rectangle: <id>,<width>,<height>,<x>,<y>
                    obj_dict = {}
                    obj_dict["id"] = int(row[0])
                    obj_dict["width"] = int(row[1])
                    obj_dict["height"] = int(row[2])
                    obj_dict["x"] = int(row[3])
                    obj_dict["y"] = int(row[4])
                    instances.append(obj_dict)
                else:
                    # Square: <id>,<size>,<x>,<y>
                    obj_dict = {}
                    obj_dict["id"] = int(row[0])
                    obj_dict["size"] = int(row[1])
                    obj_dict["x"] = int(row[2])
                    obj_dict["y"] = int(row[3])
                    instances.append(obj_dict)
        return [cls.create(**item) for item in instances]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Function to draw rectangles and squares using the turtle module

        Args:
            list_rectangles (list): List of rectangle instances
            list_squares (list): List of Square instances
        """
        # Initialize Turtle
        turt = turtle.Turtle()
        turt.screen.bgcolor("#FF8F00")
        turt.pensize(3)
        turt.shape("turtle")
        turt.color("#ffffff")
        for rectangle in list_rectangles:
            # Handle Rectangles
            turt.showturtle()
            turt.up()
            turt.goto(rectangle.x, rectangle.y)
            turt.down()
            for i in range(2):
                turt.forward(rectangle.width)
                turt.left(90)
                turt.forward(rectangle.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#000000")
        for square in list_squares:
            # Handle Squares
            turt.showturtle()
            turt.up()
            turt.goto(square.x, square.y)
            turt.down()
            for i in range(2):
                turt.forward(square.width)
                turt.left(90)
                turt.forward(square.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
