#!/usr/bin/python3

"""appends a string at the end of a text file"""

def append_write(filename="", text=""):
    
    """appent string to the end
    
    Args:
        filename (str): file name
        text (str): string
        
    Return:
        no. chars
    
    """
    
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
