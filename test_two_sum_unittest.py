import unittest
import two_sum


class TestClass(unittest.TestCase):

    # Valid tests
    def test1(self):
        self.assertEqual(two_sum.two_sum([2, 7, 11, 15], 9), [2, 7])
        self.assertEqual(two_sum.two_sum([3, 2, 4], 6), [2, 4])

    # Invalid tests (We check if unexpected output produces certain edge or unexpected output this time
    # so the tests actually pass).
    # NOTE: These assert statements require Python 3.1+ to work!
    def test2(self):
        self.assertIsNone(two_sum.two_sum([], 0))
        self.assertNotEqual(two_sum.two_sum(["3", "3"], 6), ["3", "3"])


if __name__ == "__main__":
    unittest.main()
