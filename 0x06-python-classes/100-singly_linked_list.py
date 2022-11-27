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
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """getter and setter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value != None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

"""
A class SinglyLinkedList that defines a singly linked list
"""


class SinglyLinkedList:
    """Singly Linked List"""

    def __init__(self):
        """instantiation"""
        self.__head = None

    def sorted_insert(self, value):
        """insert in sorted order"""
        NewNode = Node(value)
        if self.__head == None:
            NewNode.next_node = None
            self.__head = NewNode
        elif value < self.__head.data:
            NewNode.next = self.__head
            self.__head = NewNode
        else:
            curr = self.__head
            while (curr.next_node != None and value > curr.next_node.data):
                curr = curr.next_node
            if curr.next_node == None:
                curr.next_node = NewNode
            else:
                NewNode.next_node = curr.next_node
                curr.next_node = NewNode
    def __repr__(self):
        """string representation"""
        values = []
        while self.__head:
            values.append(str(self.__head.data))
            self.__head = self.__head.next_node
        return ('\n'.join(values))
