#!/usr/bin/env python3
"""
0-select_states.py
Lists all states from the database hbtn_0e_0_usa
"""

import pymysql
pymysql.install_as_MySQLdb()  # Makes PyMySQL work as MySQLdb
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",   # your MySQL server
        user="root",        # your username
        passwd="cavin",     # your password
        db="hbtn_0e_0_usa",# your database
        port=3306
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")  # Query all states ordered by id
    rows = cursor.fetchall()

    for row in rows:
        print(row)  # Each row is a tuple like (1, 'California')

    cursor.close()
    db.close()
