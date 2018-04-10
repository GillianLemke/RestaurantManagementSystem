#!/usr/bin/python

import MySQLdb


class Ingredients:

    def get_ingredients(self):
        # Open database connection
        db = MySQLdb.connect("localhost","root","password", db="restaurant")
        cursor = db.cursor()

        get_all = "SELECT * FROM ingredient"

        ingredients_from_db = []

        try:
            # Execute the SQL command
            cursor.execute(get_all)

            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()

            for row in results:
                name = row[0]
                supplierName= row[1]
                ingredients_from_db.append({'name': name, 'supplierName': supplierName})
        except:
            return 0

        db.close()

        return ingredients_from_db

    def add_ingredient(self, name, supplierName):
        ingredient_instance = Ingredients()
        current_ingredients = ingredient_instance.get_ingredients()

        # check to make sure a tuple with that primary key doesn't already exist
        for ingredient in current_ingredients:
            if name == ingredient["name"]:
                return 0

        add_command = ""
        if bool(name): #and bool(cost) and bool(ingredients):
            #add_command = "INSERT INTO restaurant.product(name, cost, ingredients) VALUES ('" + name + "', '" + str(cost) + "', '" + ingredients + "');"
        #elif bool(name) and bool(cost):
         #   add_command = "INSERT INTO restaurant.product(names, cost) VALUES ('" + name + "', '" + str(cost) + "');"
        #elif bool(name):
            add_command = "INSERT INTO restaurant.ingredient(ingredient_name) VALUES ('" + name + ", " + supplierName + "');"

            db = MySQLdb.connect("localhost","root","password", db="restaurant")
        cursor = db.cursor()

        try:
            # Execute the SQL command
            cursor.execute(add_command)
            db.commit()
            return {'name': name}
            db.close()
        except:
            db.rollback()
            return 1

    def delete_ingredient(self, name):
        ingredient_instance = Ingredients()
        current_ingredients = ingredient_instance.get_ingredients()

        # check to make sure a tuple with thapyt primary key doesn't already exist
        for ingredient in current_ingredients:
            print(ingredient)
            if name == ingredient["name"]:
                # remove
                add_command = "DELETE FROM restaurant.ingredient WHERE ingredient_name='" + name + "';"

                db = MySQLdb.connect("localhost","root","password", db="restaurant")
                cursor = db.cursor()

                try:
                    # Execute the SQL command
                    cursor.execute(add_command)
                    db.commit()
                    db.close()
                    return {'name': name}
                except:
                    db.rollback()
                    return 1
