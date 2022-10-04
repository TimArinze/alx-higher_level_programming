#!/usr/bin/python3


"""
A base class
"""

import json


class Base:
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dictionary to JSON string"""
        if list_dictionaries is None:
            list_dic = []
        else:
            list_dic = list_dictionaries
        return json.dumps(list_dic)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        list_o = []
        if list_objs is not None:
            for i in list_objs:
                list_o.append(cls.to_dictionary(i))
            with open(filename, "w") as f:
                f.write(cls.to_json_string(list_o))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return "[]"
        return json.loads(json_string)
