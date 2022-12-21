#!/usr/bin/python3
""" Module for script that lists all states from the db hbtn_0e_0_usa
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

    c.execute("""SELECT * FROM states
              WHERE name LIKE 'N%'
              ORDER BY states.id ASC;""")

    results = c.fetchall()
    for i in results:
        print(i)
