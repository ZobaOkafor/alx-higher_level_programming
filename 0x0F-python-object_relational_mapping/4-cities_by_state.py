#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
                "Usage: {} <username> <password> <database>"
                .format(sys.argv[0]))
        sys.exit(1)
    db = MySQLdb.connect(
            host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute(
            "SELECT cities.id, cities.name, states.name "
            "FROM cities JOIN states "
            "ON cities.state_id = states.id "
            "ORDER BY cities.id ASC"
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
