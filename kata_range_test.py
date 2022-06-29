import unittest
import kata_range

class TestKataRange(unittest.TestCase):
    def test_with_empty_string(self):
        kata_range.entered_range = ""
        kata_range.entered_range.assertRaises(SyntaxError, "Invalid range")

    def test_with_invalid_limit_symbol(self):
        kata_range.entered_range = "["
        kata_range.entered_range.assertRaises(SyntaxError, "Invalid range")
    
    def test_with_more_or_less_than_two_limits(self):
        kata_range.limits = 3
        kata_range.limits.assertRaises(IndexError, "Invalid range")
    
    def test_limit_is_not_digit(self):
        kata_range.botton_limit = "X"
        kata_range.botton_limit.assertRaises(Exception, "Invalid range")


