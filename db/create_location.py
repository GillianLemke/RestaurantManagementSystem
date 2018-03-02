#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root", db="restaurant")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# cursor.execute(add_to_table)
# db.commit()

# disconnect from server
# db.close()
