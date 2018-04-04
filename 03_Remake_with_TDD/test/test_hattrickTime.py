from unittest import TestCase
import unittest
from algorithms import ht_time


class TestHattrickTime(TestCase):
    """
    Test last Wed or Sun
    """

    def test_findLastSunOrWed_last_Sun(self):
        instance = ht_time.HattrickTime()
        result = instance.findLastSunOrWed('2018/04/03')
        self.assertEqual(result, '2018/04/01')

    def test_findLastSunOrWed_last_Wed(self):
        instance = ht_time.HattrickTime()
        result = instance.findLastSunOrWed('2018/03/31')
        self.assertEqual(result, '2018/03/28')


if __name__ == '__main__':
    unittest.main()
