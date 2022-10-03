#!/usr/bin/python3
"""
And now, the Square!
"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """A class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializing the square"""
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        """getter and setter"""
        return self.width

    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """__str__"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
