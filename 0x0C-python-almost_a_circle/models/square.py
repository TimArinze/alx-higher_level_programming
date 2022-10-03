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

    def __str__(self):
        """__str__"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
