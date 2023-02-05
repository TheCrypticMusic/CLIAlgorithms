from src.algorithms.binary_search import BinarySearch
import unittest


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.binary_search_start_of_list = BinarySearch([1, 5, 6, 7, 9, 11, 15, 17, 19, 20], 1)
        self.binary_search_size_left_of_list = BinarySearch([1, 5, 6, 7, 9, 11, 15, 17, 19, 20], 6)
        self.binary_search_size_middle_of_list = BinarySearch([1, 5, 6, 7, 9, 11, 15, 17, 19, 20], 11)
        self.binary_search_size_right_of_list = BinarySearch([1, 5, 6, 7, 9, 11, 15, 17, 19, 20], 17)
        self.binary_search_end_of_list = BinarySearch([1, 5, 6, 7, 9, 11, 15, 17, 19, 20], 20)

    def test_index_return(self):
        self.assertEqual(self.binary_search_start_of_list.run(), 0)
        self.assertEqual(self.binary_search_size_left_of_list.run(), 2)
        self.assertEqual(self.binary_search_size_middle_of_list.run(), 5)
        self.assertEqual(self.binary_search_size_right_of_list.run(), 7)
        self.assertEqual(self.binary_search_end_of_list.run(), 9)
        