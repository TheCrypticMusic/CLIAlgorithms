import unittest
from src.algorithms.linear_search import LinearSearch


class TestLinearSearch(unittest.TestCase):
    def setUp(self):
        self.test_cases_indexes = [
            {
                "list": [1, 2, 5, 6, 4, 3, 6, 2, 4, 3],
                "target": 6,
                "index": 3,
            },
            {
                "list": [10, 23, 1, 2, 3, 11, 43, 23, 32],
                "target": 10,
                "index": 0,
            },
            {
                "list": [1, 3, 5, 7, 9],
                "target": 3,
                "index": 1,
            },
            {"list": [3, 5, 7, 9, 3, 5, 7, 9], "target": 7, "index": 2},
        ]

        self.test_cases_err = [
            {
                "list": [],
                "target": 2,
                "expected_err": ValueError,
            },
            {
                "list": [1, 2, 3, 4, 5, 6, 2],
                "target": 10,
                "expected_err": ValueError,
            },
            {
                "list": [1, 2, 4, 1, 2, 3],
                "target": 5,
                "expected_err": ValueError,
            },
            {
                "list": [14],
                "target": 1,
                "expected_err": ValueError,
            },
        ]

    def test_cases_indexes(self):
        for test_case in self.test_cases_indexes:
            ls = LinearSearch(test_case["list"], test_case["target"])
            self.assertEqual(ls.target_index, test_case["index"])

    def test_cases_errs(self):
        for test_case in self.test_cases_err:
            with self.assertRaises(test_case["expected_err"]):
                LinearSearch(test_case["list"], test_case["target"])
