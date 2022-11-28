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
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter and setter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
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
        if self.__head is None:
            self.__head = NewNode
        elif self.__head.data > value:
            NewNode.next_node = self.__head
            self.__head = NewNode
        else:
            curr = self.__head
            while (curr.next_node is not None and value > curr.next_node.data):
                curr = curr.next_node
            NewNode.next_node = curr.next_node
            curr.next_node = NewNode

    def __repr__(self):
        """string representation"""
        values = []
        singlylist = self.__head
        while singlylist is not None:
            values.append(str(singlylist.data))
            singlylist = singlylist.next_node
        return ('\n'.join(values))
