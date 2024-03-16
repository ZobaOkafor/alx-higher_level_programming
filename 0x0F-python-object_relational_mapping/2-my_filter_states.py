#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def filter_states(username, password, database, state_name):
    """
    Fetches and prints states from the specified database where name
    matches the argument.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): Name of the state to search for.
    """
    # Connect to MySQL server
    db = MySQLdb.connect(
                        host="localhost", user=username,
                        passwd=password, db=database, port=3306
        )
    cur = db.cursor()

    # Execute the query
    cur.execute("""SELECT * FROM states
                WHERE name = %s ORDER BY states.id ASC""", (state_name,))

    # Fetch all the rows
    rows = cur.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
                "Usage: {} <username> <password> <database> <state_name>"
                .format(sys.argv[0])
                )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    filter_states(username, password, database, state_name)
