#!/usr/bin/python3
"""
Cities by state
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get arguments

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=3306
    )

    cursor = db.cursor()

    query = (
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )

    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()

    # Extract city names only
    cities = [row[0] for row in rows]

    print(", ".join(cities))

    cursor.close()
    db.close()
