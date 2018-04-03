from unittest import TestCase
import unittest
from algorithms import array


class TestArray(TestCase):
    """
    Test that the result sum of all numbers
    """

    def test_sum(self):
        instance = array.Array()
        result = instance.sum(6, '1 2 3 4 10 11')
        self.assertEqual(result, 31)

    """
    Tests that an exception occurs when the number of arguments is different
    """

    def test_sum_raise_exception(self):
        self.assertRaises(Exception, lambda: array.Array().sum(5, '1 2 3 4 10 11'))


if __name__ == '__main__':
    unittest.main()
