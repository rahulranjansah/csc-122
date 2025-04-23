"""Test code for the weighted die rolling functionality."""

import unittest
from src.utilities.utility import conforms_to_a_die, is_monotonically_increasing, has_negative_values


class TestUtilityFunctions(unittest.TestCase):
    """Unit tests for utility functions."""

    def test_negative_values(self):

        """
        Checks for negatgive vaues in the function
        """

        self.assertFalse(has_negative_values([]))
        self.assertTrue(has_negative_values([1,2,3,4,-4]))
        self.assertTrue(has_negative_values([2,3,5,-1,2,-2]))
        self.assertFalse(has_negative_values([1,3,5,2,1]))



    def test_conforms_to_a_die(self):

        """
        Checks for die having n-sides
        """

        self.assertTrue(conforms_to_a_die([]))
        self.assertTrue(conforms_to_a_die([2,1,3,4]))
        self.assertFalse(conforms_to_a_die([1,3,4,5,6]))
        self.assertTrue(conforms_to_a_die([1,2,3,4,5,6,7,8,9]))
        self.assertFalse(conforms_to_a_die([2,2,2]))


    def test_is_monotonically_increasing(self):

        """
        Checks if the weights are monotonically increasing
        """

        self.assertTrue(is_monotonically_increasing([]))
        self.assertTrue(is_monotonically_increasing([1,1,1,1,1]))
        self.assertTrue(is_monotonically_increasing([1,2,3,4,5]))
        self.assertTrue(is_monotonically_increasing([1,3,2,3,4]))
        self.assertTrue(is_monotonically_increasing([1,0,2,3,0]))
        self.assertFalse(is_monotonically_increasing([1,-1,2,4,1]))



if __name__ == '__main__':
    unittest.main()