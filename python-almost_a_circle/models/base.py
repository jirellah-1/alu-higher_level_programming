#!/usr/bin/python3
"""Module that defines the Base class used by all other classes."""
import json


class Base:
    """Base class that manages the id attribute of all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an instance with the given id or an automatic one."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dicts."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of list_objs to <Class>.json."""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by the JSON string json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set from dictionary."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from <Class>.json."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()
        except FileNotFoundError:
            return []
        return [cls.create(**d) for d in cls.from_json_string(content)]
