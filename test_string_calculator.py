import unittest
from string_calculator import add

class TestStringCalculator(unittest.TestCase):

    # handle empty string
    def test_empty_string(self):
        self.assertEqual(add(""), 0)


    # handle a single number
    def test_single_number(self):
        self.assertEqual(add("1"), 1)

    # handle two numbers
    def test_two_number(self):
        self.assertEqual(add("1,2"),3)
        self.assertEqual(add("10,20"),30)

    # handle multiple numbers
    def test_multiple_number(self):
        self.assertEqual(add("1,2,3,4,5"),15)
        self.assertEqual(add("10,20,30,40,50"),150)
        

if __name__ == "__main__":
    unittest.main()