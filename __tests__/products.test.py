import unittest
import sys

sys.path.insert(0, '../')
from products import Products


class ProductsTest(unittest.TestCase):
    def test_get_products(self):
        """test get method for products"""

        sample_product_from_db = {'name': 'breakfast burrito', 'cost': 2.02, 'ingredients': 'eggs, flour tortilla, refried beans'}

        product_instance = Products()
        test = product_instance.get_products()
        self.assertEqual(test[0], sample_product_from_db)

    def test_add_product(self):
        """test add product method for products"""
        product_to_add = {'name': 'cucumber', 'cost': 5.55, 'ingredients': None}

        product_instance = Products()

        # method should return object added if successful
        test = product_instance.add_product(product_to_add["name"], product_to_add["cost"], product_to_add["ingredients"])
        self.assertEqual(test, product_to_add)

        # method should return 0 if object already exists
        product_to_add_key_already_exists = {'name': 'chips', 'cost': 2.22, 'ingredients': None}
        test2 = product_instance.add_product(product_to_add_key_already_exists["name"], product_to_add_key_already_exists["cost"], product_to_add_key_already_exists["ingredients"])
        self.assertEqual(test2, 0)

    def test_delete_product(self):
        """test delete product method for products"""
        product_key_to_delete = 'cucumber'

        product_instance = Products()

        # method should return object added if successful
        test = product_instance.delete_product(product_key_to_delete)
        self.assertEqual(test, {'name': product_key_to_delete})

        # method should return 0 if the key does not exist
        product_key_to_delete_2 = 'apple pie'
        test2 = product_instance.delete_product(product_key_to_delete_2)
        self.assertEqual(test2, 0)


if __name__ == '__main__':
    unittest.main()
