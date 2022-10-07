#!/usr/bin/python3


"""
A base class
"""

import json
import csv


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
        """JSON string to file"""
        filename = cls.__name__ + ".json"
        list_o = []
        if list_objs is not None:
            for i in list_objs:
                list_o.append(cls.to_dictionary(i))
            with open(filename, 'w') as f:
                f.write(cls.to_json_string(list_o))
        return filename

    @staticmethod
    def from_json_string(json_string):
        """JSON string to dictionary"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Dictionary to Instance"""
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 1)
        elif cls.__name__ == "Square":
            dummy = cls(2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Files to instance"""
        filename = cls.__name__ + ".json"
        list_i = []
        if filename is None:
            return list_i

        with open(filename, 'r') as f:
            list_i = cls.from_json_string(f.read())
        for i in range(len(list_i)):
            list_i[i] = cls.create(**list_i[i])
        return list_i

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save to csv file"""
        filename = cls.__name__ + ".csv"
        list_i = []
        if list_objs is not None:
            for line in list_objs:
                list_i.append(cls.to_dictionary(line))
            with open(filename, 'w') as f:
                f.write(cls.to_json_string(list_i))

    @classmethod
    def load_from_file_csv(cls):
        """load from csv file"""
        filename = cls.__name__ + ".csv"
        list_i = []
        if filename is None:
            return list_i
        else:
            with open(filename, 'r') as f:
                list_i = cls.from_json_string(f.read())
            for i in range(len(list_i)):
                list_i[i] = cls.create(**list_i[i])
            return list_i

