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

    def test_bottomlimit_greater_than_toplimit(self):
        kata_range.botton_limit = 7
        kata_range.top_limit = 6
        kata_range.botton_limit.assertRaises(Exception, "Invalid range")

    def test_range_to_string(self):
        kata_range.entered_range = [2,3]
        kata_range.entered_range.to_string().assertEqual("2,3")

if __name__ == "__main__":
    unittest.main()

