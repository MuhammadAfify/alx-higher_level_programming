#!/usr/bin/python3

"""takes in a URL, sends a request to the URL and displays the value"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    """takes in a URL, sends a request to the URL and displays the value"""
    with urllib.request.urlopen(argv[1]) as response:
        html_id = response.info().get('X-Request-Id')
        print(html_id)
