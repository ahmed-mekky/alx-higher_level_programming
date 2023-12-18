#!/usr/bin/python3
import MySQLdb
import sys

"""This script is doing something"""

if __name__ == '__main__':
    """
    Access to the database
    """
    args = sys.argv

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=args[1],
        passwd=args[2],
        db=args[3],
        charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
