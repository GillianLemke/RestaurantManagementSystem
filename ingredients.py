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
                ingredients_from_db.append({'name': name})
        except:
            return 0

        db.close()

        return ingredients_from_db

    def add_ingredient(self, name):
        ingredient_instance = Ingredients()
        current_ingredients = ingredient_instance.get_ingredients()

        print name
        print bool(name)
        # print cost
        # print bool(name)

        # check to make sure a tuple with that primary key doesn't already exist
       # for product in current_ingredients:
           # if name == product["name"]:
               # return 0

        add_command = ""
        if bool(name):
            #add_command = "INSERT INTO restaurant.ingredients(name, cost, ingredients) VALUES ('" + name + "', '" + str(cost) + "', '" + ingredients + "');"
       # elif bool(name) and bool(cost):
          #  add_command = "INSERT INTO restaurant.ingredients(name, cost) VALUES ('" + name + "', '" + str(cost) + "');"
       # elif bool(name):
            add_command = "INSERT INTO restaurant.ingredients(name) VALUES ('" + name + "');"

        db = MySQLdb.connect("localhost", "root", "password", db="restaurant")
        cursor = db.cursor()

        try:
            # Execute the SQL command
            cursor.execute(add_command)
            return {'name': name}
        except:
            # return 1 if sql error
            return 1


        # TODO: check to make sure ingredients exist


        return -1

ingredient_instance = Ingredients()
ingredient_instance.get_ingredients()