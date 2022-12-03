#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
Your script should take 4 arguments: mysql username, mysql password,
database name and state name (SQL injection free!)
"""


import sys
import MySQLdb


if __name__ == "__main__":
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                          host="localhost", port=3306)
    cur = con.cursor()
    cur.execute("SELECT *\
            FROM cities INNER JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC")
    query_rows = cur.fetchall()
    city_list = []
    for row in query_rows:
        if row[-1] == sys.argv[4]:
            city_list.append(row[2])
    print(', '.join(city_list))
