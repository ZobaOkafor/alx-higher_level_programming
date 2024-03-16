#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def select_states(username, password, database):
    """
    Fetches and prints states from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
    """
    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    select_states(username, password, database)
