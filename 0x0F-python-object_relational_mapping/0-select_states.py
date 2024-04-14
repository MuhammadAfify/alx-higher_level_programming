#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

for sys import argv
import MYSQLdb

if __name__ == "__main__":
        db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    curs = db.cursor()
    curs.excute("SELECT * FROM `states`")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()
