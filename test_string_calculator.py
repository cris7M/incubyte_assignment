import unittest
from string_calculator import add

class TestStringCalculator(unittest.TestCase):

    # handle empty string
    def test_empty_string(self):
        self.assertEqual(add(""), 0)


    # handle a single number
    def test_single_number(self):
        self.assertEqual(add("1"), 1)


if __name__ == "__main__":
    unittest.main()