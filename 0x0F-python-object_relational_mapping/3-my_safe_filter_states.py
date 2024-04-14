#!/usr/bin/python3
"""Same as last task but safe from MySQL injections"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    # make a connection to the database
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s", [argv[4]])

    rows = cur.fetchall()
    for i in rows:
        print(i)

    cur.close()
    conn.close()
