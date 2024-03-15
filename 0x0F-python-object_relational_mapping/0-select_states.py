#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """


import sys
import MySQLdb

if __name__ == "__main__":
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        [print(state) for state in cursor.fetchall()]
        db.close()
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
