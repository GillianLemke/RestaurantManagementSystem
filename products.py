#!/usr/bin/python

import MySQLdb


class Products:

    def get_products(self):
        # Open database connection
        db = MySQLdb.connect(host="localhost", user="root", passwd="secret", db="restaurant", port=33306)
        cursor = db.cursor()

        get_all = "SELECT * FROM product"

        products_from_db = []
        print 'here'

        try:
            # Execute the SQL command
            print 'in try'
            cursor.execute(get_all)
            print 'after exectue'
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            print 'after fetch'
            for row in results:
                print 'in for loop'
                name = row[0]
                cost = row[1]
                ingredients = row[2]
                products_from_db.append({'name': name, 'cost': cost, 'ingredients': ingredients})
        except:
            print 'except'
            return 0

        db.close()

        return products_from_db


print 'start'
product_instance = Products()
product_instance.get_products()
