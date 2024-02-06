#!/usr/bin/python3

"""writes an Object to a text file, using a JSON representation"""

import json

def save_to_json_file(my_obj, filename):
    
    """returns Python data structure"""
    
    with open(filename, "w") as f:
        json.dump(my_obj, f)
