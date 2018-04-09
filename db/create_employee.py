#!/usr/bin/python

# TODO: ADD LOCATION ATTRIBUTE

import MySQLdb

# status = ['PARTTIME', 'FULLTIME', 'RETIRED', 'TERMINATED', 'MANAGEMENT']

# Open database connection
db = MySQLdb.connect("localhost","root", db="restaurant")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Create table as per requirement
sql = "CREATE TABLE EMPLOYEE (NAME CHAR(40) NOT NULL, EMPLOYEE_ID INT NOT NULL, WAGE FLOAT, STATUS ENUM('PARTTIME', 'FULLTIME', 'MANAGEMENT', 'TERMINATED', 'RETIRED'), LOCATION FOREIGN KEY (location_id) REFERENCES locations(id) );"

add_to_table = "INSERT into employee (name, wage, status) values ('Gillian', 10.2, 'TERMINATED');"

# cursor.execute(sql)
cursor.execute(add_to_table)
db.commit()

# disconnect from server
db.close()
