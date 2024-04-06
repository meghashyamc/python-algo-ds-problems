import unittest
from strings import reverse_string


class TestReverseStringByWord(unittest.TestCase):
    def test_reverse_string_by_word(self):
        test_cases = [("the sky is blue","blue is sky the"), ("this is   ib    ", "ib is this")]
        for input, expected in test_cases:
            self.assertEqual(reverse_string.reverse_string_by_word(input), expected)