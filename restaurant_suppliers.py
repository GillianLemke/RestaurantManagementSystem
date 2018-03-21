#!/usr/bin/python

# TODO: ADD SUPPLIER ATTRIBUTE



import MySQLdb


# Open database connection

db = MySQLdb.connect("localhost","root","password", db="restaurant")



# prepare a cursor object using cursor() method

cursor = db.cursor()



# Create table as per requirement

show_supplier = "SELECT * FROM supplier"

# cursor.execute(sql)

cursor.execute(show_supplier)

# Fetch a single row using fetchone() method.
rows = cursor.fetchall()
for row in rows:
    print "Database row : %s " % row

db.commit()

# disconnect from server(s)

db.close()