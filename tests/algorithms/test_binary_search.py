import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.algorithms.binary_search import BinarySearch


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.test_cases_indexes = [
            {
                "list": [1, 5, 6, 7, 9, 11, 15, 17, 19, 20],
                "target": 1,
                "expected_index": 0,
            },
            {
                "list": [1, 5, 6, 7, 9, 11, 15, 17, 19, 20],
                "target": 6,
                "expected_index": 2,
            },
            {
                "list": [1, 5, 6, 7, 9, 11, 15, 17, 19, 20],
                "target": 11,
                "expected_index": 5,
            },
            {
                "list": [1, 5, 6, 7, 9, 11, 15, 17, 19, 20],
                "target": 17,
                "expected_index": 7,
            },
            {
                "list": [1, 5, 6, 7, 9, 11, 15, 17, 19, 20],
                "target": 20,
                "expected_index": 9,
            },
        ]
        self.test_cases_err = [
            {
                "list": [],
                "target": 1,
                "expected_err": ValueError,
            },
            {
                "list": [1],
                "target": 2,
                "expected_err": ValueError,
            },
            {
                "list": [1, 2, 3, 4, 5, 6, 1, 2],
                "target": 2,
                "expected_err": ValueError,
            },
            {
                "list": [1, 2, 3, 4, 5, 6, 7, 8, 9],
                "target": 0,
                "expected_err": ValueError,
            },
            {
                "list": [1, 2, 3, 4, 6, 7, 8, 9],
                "target": 5,
                "expected_err": ValueError,
            },
        ]

    def test_binary_search_indexes(self):
        for test_case in self.test_cases_indexes:
            bs = BinarySearch(test_case["list"], test_case["target"])
            self.assertEqual(bs.run(), test_case["expected_index"])

    def test_binary_search_exceptions(self):
        for test_case in self.test_cases_err:
            with self.assertRaises(test_case["expected_err"]):
                BinarySearch(test_case["list"], test_case["target"])


if __name__ == "__main__":
    unittest.main()
