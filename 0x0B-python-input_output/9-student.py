#!/usr/bin/python3
"""
A class Student that defines a student
"""


class Student:
    """ Student to JSON """

    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dictionary representation"""
        return self.__dict__
