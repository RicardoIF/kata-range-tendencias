import unittest
import kata_range

class TestKataRange(unittest.TestCase):
    def test_with_empty_string(self):
        entered_range = ""
        entered_range.assertRaises(SyntaxError, "Invalid range")

    def test_with_invalid_limit_symbol(self):
        entered_range = "["
        entered_range.assertRaises(SyntaxError, "Invalid range")
    
    def test_with_more_or_less_than_two_limits(self):
        limits = 3
        limits.assertRaises(IndexError, "Invalid range")
    
    


