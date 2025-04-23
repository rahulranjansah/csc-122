# """
#    *
#    * Id factory Class
#    *
#    * @author Rahul Ranjan Sah & Samriddha GC
#    * @date   02/12/2025
# """

import unittest
from src.utilities.id_factory import IdFactory


class TestIdFactory(unittest.TestCase):

    """Unit tests for next functions.
    """

    def test_next(self):
        """Next function count testing"""
        a = IdFactory()

        self.assertEqual(next(a), 0)
        self.assertEqual(next(a), 1)
        self.assertEqual(next(a), 2)
        self.assertEqual(next(a), 3)
        self.assertNotEqual(next(a), 5)