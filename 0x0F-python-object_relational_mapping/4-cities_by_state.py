#!/usr/bin/python3
""" Module for script that lists cities from the db hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    u_name = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    db = MySQLdb.connect(
            user=u_name, passwd=pwd, database=db, host='localhost', port=3306)
    c = db.cursor()

    c.execute("""SELECT cities.id, cities.name, states.name FROM cities
              INNER JOIN states
              ON cities.state_id = states.id
              ORDER BY cities.id ASC;""")

    results = c.fetchall()
    for i in results:
        print(i)
