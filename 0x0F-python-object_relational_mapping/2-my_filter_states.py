#!/usr/bin/python3
"""This script is doing something"""

import MySQLdb
import sys


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
        db=args[3])

    cur = conn.cursor()

    cur.execute(f"SELECT * FROM states WHERE name = '{args[4]}'\
                ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
