#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM cities
                    INNER JOIN states ON cities.state_id = states.id""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
