#!/usr/bin/python3
""" A script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    u_name = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(
            user=u_name, passwd=pwd, database=db, host='localhost', port=3306)
    c = db.cursor()

    c.execute("""SELECT cities.name FROM cities
              INNER JOIN states
              ON cities.state_id = states.id
              WHERE states.name = %s
              ORDER BY cities.id ASC;""", (state,))

    results = c.fetchall()
    count = 0
    for i in results:
        for x in i:
            if count != 0:
                print(", ", end="")
            print(x, end="")
            count += 1
    print()
