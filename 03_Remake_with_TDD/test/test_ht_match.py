from unittest import TestCase
import unittest
from algorithms import ht_match

class TestHattrickMatch(TestCase):
    """
    Test Home matchList
    """
    def test_home_findMatchList(self):
        instance = ht_match.HattrickMatch()
        result = instance.findMatchList('2018-04-25/match.html', 'mydatabase')
        for match in result:
            print(match)