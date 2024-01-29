#!/usr/bin/python3

"""class name is Rectangle"""
class Rectangle:
    """represent rectangle"""

    def __init__(self, width = 0, height = 0):
        """new rectangle class"""
        self.width = width
        self.height = height

        @property
        def width(self):
            """get and assign the width"""
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
                if value < 0:
                    raise TypeError("width must be >= 0")
                self.__width = value

        @property
        def height(self):
            """get and assign the height"""
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
                if value < 0:
                    raise TypeError("height must be >= 0")
                    self.__height = value
