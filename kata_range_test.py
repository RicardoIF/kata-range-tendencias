import unittest
import kata_range

class TestKataRange(unittest.TestCase):
    def test_with_invalid_symbol(self):
        entered_range = ""
        entered_range.assertRaises(SyntaxError, "Invalid range")

    def test_with_range(self):
        entered_range = ""
        entered_range.assertRaises(SyntaxError, "Invalid range")

