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

    # handle new line as delimeter 
    def test_newline_as_delemeter(self):
        self.assertEqual(add("1\n2,3"),6)
        self.assertEqual(add("10\n20,30"),60)

    # Support different delimiters
    def test_custom_delimeter(self):
        self.assertEqual(add("//;\n1;2"),3)
        self.assertEqual(add("//|\n1|2|3"),6)

    # handle negative number
    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            add("1,-2,3,-4")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2, -4")


if __name__ == "__main__":
    unittest.main()