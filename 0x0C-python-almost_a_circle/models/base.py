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

    def save_to_file(self, list_objs):
        """JSON string to file"""
        with open("{}.json".format(self), "w") as outfile:
            json.dump(list_objs, outfile)
