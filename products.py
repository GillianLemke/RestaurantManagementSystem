#!/usr/bin/python

import MySQLdb


class Products:

    def get_products(self):
        # Open database connection
        db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="secret", db="restaurant", port=33306)
        cursor = db.cursor()

        get_all = "SELECT * FROM product"

        products_from_db = []

        try:
            # Execute the SQL command
            cursor.execute(get_all)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            for row in results:
                name = row[0]
                cost = row[1]
                ingredients = row[2]
                products_from_db.append({'name': name, 'cost': cost, 'ingredients': ingredients})
        except:
            return 0

        db.close()

        return products_from_db

    def add_product(self, name, cost, ingredients):
        product_instance = Products()
        current_products = product_instance.get_products()

        # check to make sure a tuple with that primary key doesn't already exist
        for product in current_products:
            if name == product["name"]:
                return 0


        return 3



product_instance = Products()
product_instance.get_products()
