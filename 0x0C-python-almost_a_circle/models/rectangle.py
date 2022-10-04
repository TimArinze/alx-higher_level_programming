#!/usr/bin/python3
"""
class Rectangle that inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """ First Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiation"""
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter and Setter"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format("width"))
        elif value <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.__width = value

    @property
    def height(self):
        """getter and setter"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format("height"))
        elif value <= 0:
            raise ValueError("{} must be > 0".format("height"))
        self.__height = value

    @property
    def x(self):
        """getter and setter"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format("x"))
        elif value < 0:
            raise ValueError("{} must be >= 0".format("x"))
        self.__x = value

    @property
    def y(self):
        """getter and setter"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format("y"))
        elif value < 0:
            raise ValueError("{} must be >= 0".format("y"))
        self.__y = value

    def area(self):
        """ Area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Representation of Rectangle with #"""
        if self.area == 0:
            print()
        for k in range(self.y):
            print("")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """method that returns ..."""
        string = "[Rectangle] ({}) {}/{} - {}/{}"
        return string.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Using args"""
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """to dictionary"""
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["width"] = self.width
        dictionary["height"] = self.height
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        return dictionary
