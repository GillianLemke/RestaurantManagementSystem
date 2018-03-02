import unittest
import sys

sys.path.insert(0, '../')
from products import Products


class ProductsTest(unittest.TestCase):
    def test_get_products(self):
        """test get method for products"""

        sample_product_from_db = {'name': 'apple', 'cost': 4.44, 'ingredients': None}

        print sample_product_from_db
        test = Products.get_products()
        print test
        # self.assertEqual(test[0], sample_product_from_db)



if __name__ == '__main__':
    unittest.main()
