#!/usr/bin/python3
"""
    takes argument and displays values in
    the states table where name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute ("SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4]))
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()
