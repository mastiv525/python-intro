import unittest
from my_awesome_lib.data_utils import flatten_list, unique_items

class TestDataUtils(unittest.TestCase):
    def test_flatten_list_simple(self):
        self.assertEqual(flatten_list([[1, 2], [3, 4]]), [1, 2, 3, 4])

    def test_flatten_list_with_items(self):
        self.assertEqual(flatten_list([1, [2, 3], 4]), [1, 2, 3, 4])

    def test_unique_items(self):
        self.assertEqual(unique_items([1, 2, 2, 3, 1]), [1, 2, 3])

    def test_unique_items_empty(self):
        self.assertEqual(unique_items([]), [])
