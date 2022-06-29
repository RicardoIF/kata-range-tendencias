import unittest
from kata_range import Range

class TestKataRange(unittest.TestCase):
    def test_with_empty_string(self):
        entered_range = ""
        rnge = Range(entered_range)
        rnge.assertRaises(SyntaxError, "Invalid range")

    def test_bottomlimit_greater_than_toplimit(self):
        entered_range = "(8, 6]"
        rnge = Range(entered_range)
        rnge.assertRaises(ValueError, "Invalid range")

    def test_valid_input_range(self):
        entered_range = "[2, 5]"
        rnge = Range(entered_range)
        rnge.assertIsInstance(rnge, Range)

class TestGetAllPoints(unittest.TestCase):
    def test_get_all_points(self):
        entered_range = "[3, 7]"
        rnge = Range(entered_range)
        self.assertEqual(rnge.getAllPoints(), [3, 4, 5, 6, 7])

class TestEndPoints(unittest.TestCase):
    def test_get_all_points(self):
        entered_range = "(1, 3]"
        rnge = Range(entered_range)
        self.assertEqual(rnge.endPoints, [2,3])

class TestOverlaps(unittest.TestCase):
    def test_range_overlaps_true(self):
        first_range = Range("[4, 10]")
        second_range = Range("[4, 12]")
        self.assertEqual(first_range.overlapsRange(second_range), True)
    def test_range_overlaps_true(self):
        first_range = Range("[4, 10]")
        second_range = Range("[12, 22]")
        self.assertEqual(first_range.overlapsRange(second_range), False)

class TestToString(unittest.TestCase):
    def test_range_to_string(self):
        rnge = Range([3, 4])
        expectedResult = "[3, 4]"
        self.assertEqual(rnge, expectedResult)

if __name__ == "__main__":
    unittest.main()