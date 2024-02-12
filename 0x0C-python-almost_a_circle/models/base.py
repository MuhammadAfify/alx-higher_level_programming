#!/usr/bin/python3

"""class definition"""

class Base:

    """represent base model"""

    __nb_objects = 0
    def __init__(self, id=None):

        """iniate new base"""

        if id is not None:
            Base.id = id
        else:
            Base.__nb_objects += 1
