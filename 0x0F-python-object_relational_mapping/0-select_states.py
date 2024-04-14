#!/usr/bin/python3
"""lists all states from the database"""

form sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host = "localhoast", port = 3306, user = argv[1],
            passwd = argv[2], db = argv[3])
    curs = conn.cursor()
    curs.execute("SELECT * FROM states")

    rows = curs.fetchall()
    for i in rows:
        print(i)

    curs.close()
    conn.close()
