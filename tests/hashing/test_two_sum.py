import unittest
from hashing import two_sum

class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        test_cases = [(([2,7,11,15,9],9),[1,2]),(([15,9],9),[]),(([],9),[]), (([5,5,5,5,5],  10), [1,2]), (([ 10, -3, 5, -7, -4, 5, 6, -7, 8, -5, 8, 0, 8, -5, -10, -1, 1, -6, 4, -1, -2, -2, 10, -2, -4, -7, 5, 1, 7, -10, 0, 5, 8, 6, -8, 8, -8, -8, 3, -9, -10, -5, -5, -10, 10, -4, 8, 0, -6, -2, 3, 7, -5, 5, 1, -7, 0, -5, 1, -3, 10, -4, -3, 3, 3, 5, 1, -2, -6, 3, -4, 10, -10, -3, -8, 2, -2, -3, 0, 10, -6, -8, -10, 6, 7, 0, 3, 9, -10, -7, 8, -7, -7 ], -2), [3,4])]
        for input, expected in test_cases:
            self.assertEqual(two_sum.get_numbers_with_given_sum(*input), expected)

        