import unittest
import reverse_sentence


class TestClass(unittest.TestCase):

    # Valid tests
    def test1(self):
        self.assertEqual(reverse_sentence.rev_sen("My name is Khai Phan"), "Phan Khai is name My")
        self.assertEqual(reverse_sentence.rev_sen("This is a test"), "test a is This")

    # Invalid tests (results in failure)
    def test2(self):
        self.assertEqual(reverse_sentence.rev_sen(123), "321")
        self.assertEqual(reverse_sentence.rev_sen(1.12), "21.1")


if __name__ == "__main__":
    unittest.main()
