#!/usr/bin/python3
"""
A class Node that defines a node of a singly linked list
"""


class Node:
    """ Node"""

    def __init__(self, data, next_node=None):
        """Instantiation"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter and setter"""
        return self.__data

    @data.setter
    def data(self, value):
        if type(data) != int:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """getter and setter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if next_node != None or next_node != Node:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    """Singly Linked List"""

    def __init__(self):
        """instantiation"""

    def sorted_insert(self, value):
