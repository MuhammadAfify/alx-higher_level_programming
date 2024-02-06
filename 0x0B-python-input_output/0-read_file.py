#!/usr/bin/python3

"""reads a text file (UTF8) and prints it to stdout"""

def read_file(filename=""):
    """open the file and print the content"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
