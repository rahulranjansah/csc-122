
# """
#    *
#    * Test Sorting
#    *
#    * @author Rahul Ranjan Sah & Samriddha
#    * @date   03/19/2025
# """

from collections.abc import Callable
import unittest
import src.utilities.sorts.sorting as sorting
import random

class TestSorting(unittest.TestCase):


    def run_sort(self, technique : Callable, iterations = 100):

        lst = []
        for i in range(iterations):
            lst.append(i)

        lst_copy = lst.copy()

        # reversed list sort
        rev_list = lst_copy[::-1]
        technique(rev_list)
        self.assertEqual(rev_list, lst)

        # normal list
        normal_lst = lst_copy
        self.assertEqual(normal_lst, lst)

        random.shuffle(lst_copy)
        technique(lst_copy)

        self.assertEqual(lst_copy, lst)



    def test_sorts(self):
        self.run_sort(sorting.sinking_sort)
        self.run_sort(sorting.max_selection_sort)