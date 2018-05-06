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

    """
    Test MatchList is Home
    """
    def test_is_matchList_home(self):
        instance = ht_match.HattrickMatch()
        self.assertTrue(instance.isHome('2018-04-25/match.html', 'mydatabase'), 'match is not Home')