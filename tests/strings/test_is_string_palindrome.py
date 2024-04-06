import unittest
from strings  import is_string_palindrome


class TestIsStringPalindrome(unittest.TestCase):
    def test_is_string_palindrome(self):
        test_cases = [("hello", 0),("malayalam", 1),("r  !?, ac ecar",1),("",1), ("a",1), ("A man, a plan, a canal: Panama", 1) ]
        for inputs, expected in  test_cases:
            self.assertEqual(is_string_palindrome.is_string_palindrome
(inputs), expected)
    