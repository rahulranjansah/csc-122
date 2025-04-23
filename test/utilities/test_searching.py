# """
#    *
#    * Test Searching
#    *
#    * @author Rahul Ranjan Sah & Samriddha
#    * @date   03/18/2025
# """


from collections.abc import Callable

import unittest

import src.utilities.searching as searching

class TestSearching(unittest.TestCase):

    def __run_search(self, technique : Callable):

        """Exhaustive search
        Examples:
        technique(lst, 5)
        technique(lst, 100)
        technique(lst, 92)
        technique(lst, 106)
        technique(lst, 109)
        technique(lst, -3)"""

        lower = 0
        upper = 103
        step = 3

        # Create a sorted list
        lst = list(range(lower, upper, step))

        for val in lst:

            # Search for each item in the list
            self.assertEqual(technique(lst, val), lst.index(val))

            # Search for each item NOT in the list
            self.assertEqual(technique(lst, val+1), -len(lst)-1)
            self.assertEqual(technique(lst, val+2), -len(lst)-1)
            self.assertNotEqual(technique(lst, val+1), lst.index(val))
            self.assertNotEqual(technique(lst, val+2), lst.index(val))

            # Search for items outside the list
            self.assertEqual(technique(lst, val+103), -len(lst) - 1)
            self.assertEqual(technique(lst, -val-1), -len(lst) - 1)
            self.assertNotEqual(technique(lst, val+103), lst.index(val))
            self.assertNotEqual(technique(lst, -val-1), lst.index(val))

    def test_search(self):
        self.__run_search(searching.binary_search)
        self.__run_search(searching.trinary_search)

    def __run_search_valid_index(self, technique : Callable):
        '''
        Runs tests for valid index search
        Examples:
        technique(lst, 2)
        technique(lst, 8)
        technique(lst, 98)
        '''

        lower = 0
        upper = 103
        step = 3

        # Create a sorted list
        lst = list(range(lower, upper, step))

        for val in lst:
            self.assertEqual(technique(lst, val+1), lst.index(val) + 1)
            self.assertEqual(technique(lst, val+2), lst.index(val) + 1)
            self.assertEqual(technique(lst, -val), 0)
            self.assertEqual(technique(lst, val+103), len(lst))

    def test_search_less_than(self):
        self.__run_search_valid_index(searching.binary_search_valid_index)
        self.__run_search_valid_index(searching.trinary_search_valid_index)
