from unittest import TestCase
import unittest
from algorithms import ht_match

class TestHattrickMatch(TestCase):
    """
    Test MatchList is Home
    """
    def test_is_matchList_home(self):
        instance = ht_match.HattrickMatch()
        self.assertTrue(instance.isHome('2018-04-25/match.html', 'mydatabase'), 'match is not Home')

    """
    Test MatchList is Away
    """
    def test_is_matchList_away(self):
        instance = ht_match.HattrickMatch()
        self.assertFalse(instance.isHome('2018-04-18/match.html', 'mydatabase'), 'match is not Away')

    """
    Test Home matchList
    """
    def test_home_findMatchList(self):
        instance = ht_match.HattrickMatch()
        filePath = '2018-04-25/match.html'
        result = instance.findMatchList(filePath, 'mydatabase')
        print(filePath)
        for match in result:
            print(match)

    """
    Test Away matchList
    """
    def test_away_findMatchList(self):
        instance = ht_match.HattrickMatch()
        filePath = '2018-04-18/match.html'
        result = instance.findMatchList(filePath, 'mydatabase')
        print(filePath)
        for match in result:
            print(match)
