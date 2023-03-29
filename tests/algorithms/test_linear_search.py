import unittest
from src.algorithms.linear_search import LinearSearch


class TestLinearSearch(unittest.TestCase):
    def setUp(self):
        self.test_cases_indexes = [
            {
                "list": [1, 2, 5, 6, 4, 3, 6, 2, 4, 3],
                "target": 6,
                "is_found": True,
            },
            {
                "list": [10, 23, 1, 2, 3, 11, 43, 23, 32],
                "target": 4,
                "is_found": False,
            },
        ]

    def test_cases_indexes(self):
        for test_case in self.test_cases_indexes:
            ls = LinearSearch(test_case["list"], test_case["target"])
            self.assertEqual(ls.run(), test_case["is_found"])
