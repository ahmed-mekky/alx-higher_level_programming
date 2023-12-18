#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    args = sys.argv

    conn = MySQLdb.connect(host="localhost", port=3306, user=f"{args[1]}", passwd=f"{args[2]}", db=f"{args[3]}", charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
