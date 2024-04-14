#!/usr/bin/python3
# script that lists all states from the database hbtn_0e_0_usa

import sys
import MYSQLdb

if __name__ == "__main__":
    conn = MYSQLdb.connect (user = sys.argv[1], password = sys.argv[2], db = sys.argv[3])
    curs = conn.cursor()
    curs.excute("SELECT * FROM `states`")
    [print(state) for state in curs.fetchall()]
