#!/usr/bin/python

import MySQLdb


class Suppliers:

    def get_suppliers(self):
        # Open database connection
        db = MySQLdb.connect("localhost","root","password", db="restaurant")
        cursor = db.cursor()

        get_all = "SELECT * FROM suppliers"

        suppliers_from_db = []

        try:
            # Execute the SQL command
            cursor.execute(get_all)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            for row in results:
                name = row[0]
                contact_name = row[1]
                contact_phone = row[2]
                suppliers_from_db.append({'name': name, 'contact_name': contact_name, 'contact_phone': contact_phone})
        except:
            return 0

        db.close()

        return suppliers_from_db

    def add_supplier(self, name, contact_name, contact_phone):
        supplier_instance = Suppliers()
        current_suppliers = supplier_instance.get_suppliers()

        print name
        print bool(name)
        print contact_name
        print bool(name)
        print contact_phone
        print bool(contact_phone)

        # check to make sure a tuple with that primary key doesn't already exist
       # for product in current_ingredients:
           # if name == product["name"]:
               # return 0

        add_command = ""
        #if bool(name) and bool(contact_name) and bool(contact_phone):
         #   add_command = "INSERT INTO restaurant.suppliers(name, contact_name, contact_number) VALUES ('" + name + "', '" + contact_name + "', '" + contact_number + "');"
       # elif bool(name) and bool(cost):
          #  add_command = "INSERT INTO restaurant.ingredients(name, cost) VALUES ('" + name + "', '" + str(cost) + "');"
       # elif bool(name):
            #add_command = "INSERT INTO restaurant.suppliers(name) VALUES ('" + name + "');"

        db = MySQLdb.connect("localhost", "root", "password", db="restaurant")
        cursor = db.cursor()

        try:
            # Execute the SQL command
            cursor.execute(add_command)
            return {'name': name}
        except:
            # return 1 if sql error(s)
            return 1


        # TODO: check to make sure ingredients exist


        return -1

ingredient_instance = Suppliers()
ingredient_instance.get_suppliers()