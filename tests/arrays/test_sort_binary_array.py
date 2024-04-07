import unittest
from arrays import sort_binary_array


class TestSortBinaryArray(unittest.TestCase):
    def test_sort_binary_array(self):
        test_cases = [([1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), ([1, 0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 1, 1, 1]), ([], []), ([1,1,1], [1,1,1]), ([0,0,1], [0,0,1])] 
        for input, expected in test_cases:
            self.assertEqual(sort_binary_array.sort_binary_arr(input), expected)