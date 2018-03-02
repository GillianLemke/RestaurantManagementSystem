#!/usr/bin/python

# TODO: ADD LOCATION ATTRIBUTE

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "root", "secret", "restaurant")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Create table as per requirement
sql = "CREATE TABLE `restaurant`.`product` (`name` VARCHAR(50) NOT NULL, `cost` DOUBLE NULL DEFAULT 0.00, `ingredients` VARCHAR(50) NULL, PRIMARY KEY (`name`));"
cursor.execute(sql)

db.commit()

# disconnect from server
db.close()