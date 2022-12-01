#!/usr/bin/python3

import sys
import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd=sys.argv[2], db="my_db", charset="utf8")

if __name__ == "__main__":
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[0] == 'N':
            print(row)
cur.close()
conn.close()
