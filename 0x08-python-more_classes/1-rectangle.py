#!/usr/bin/python3

"""class name is Rectangle"""
class Rectangle:
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
            if type(value) is not int:
                raise TypeError("Width has to be integer")
                if value < 0:
                    raise TypeError("width has to be greater than zero")
                self.__width = value

        @property
        def height(self):
            """get and assign the height"""
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) is not int:
                raise TypeError("height has to be integer")
                if value < 0:
                    raise TypeError("height has to be greater than zero")
                    self.__height = value
