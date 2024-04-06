import unittest
from twopointers import max_streak_of_ones

class TestMaxStreakOfOnes(unittest.TestCase):
    def test_get_max_continuous_ones_after_flipping_zeroes(self):
        test_cases = [(([1, 1, 0, 1, 1, 0, 0, 1, 1, 1 ],1),[0,1,2,3,4]),(([1, 0, 0, 0, 1, 0, 1], 2),[3,4,5,6]), (([ 0, 1, 1, 1 ], 0), [1,2,3]), (([1,1,0],2), [0,1,2])]
        for input, expected in test_cases:
            self.assertEqual(max_streak_of_ones.get_max_continuous_ones_after_flipping_zeroes(*input), expected)