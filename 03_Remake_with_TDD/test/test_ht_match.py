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
    """
    Test match_dict_list to match_str_list
    """
    def test_match_dict_list_to_match_str_list(self):
        instance = ht_match.HattrickMatch()
        filePath = '2018-04-18/match.html'
        match_dict_list = instance.findMatchList(filePath, 'mydatabase')
        match_str_list = instance.matchDictListToMatchStrList(match_dict_list)
        for str_line in match_str_list:
            print(str_line)
