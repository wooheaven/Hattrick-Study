from unittest import TestCase
import unittest
from algorithms import ht_match

class TestHattrickMatch(TestCase):
    """
    Test MatchList is Home
    """
    def test_is_matchList_home(self):
        instance = ht_match.HattrickMatch()
#        self.assertTrue(instance.isHome('2018/04/25/match.html', 'mydatabase'), 'match is not Home')

    """
    Test MatchList is Away
    """
    def test_is_matchList_away(self):
        instance = ht_match.HattrickMatch()
#        self.assertFalse(instance.isHome('2018/04/18/match.html', 'mydatabase'), 'match is not Away')

    """
    Test Home matchList
    """
    def test_home_findMatchList(self):
        instance = ht_match.HattrickMatch()
        filePath = '2018/04/25/match.html'
        result = instance.findMatchList(filePath, 'mydatabase', 'player')
        print(filePath)
        for match in result:
            print(match)

    def test_home_findMatchList_2019_05_08_LK(self):
        instance = ht_match.HattrickMatch()
        filePath = '2019/05/08/match.html'
        result = instance.findMatchList(filePath, 'mydatabase', 'player_tmp')
        print(filePath)
        for match in result:
            print(match)

    def test_home_findMatchList_2019_05_15_HD(self):
        instance = ht_match.HattrickMatch()
        filePath = '2019/05/15/match_HD.html'
        result = instance.findMatchList(filePath, 'mydatabase2', 'player_tmp')
        print(filePath)
        for match in result:
            print(match)

    """
    Test Away matchList
    """
    def test_away_findMatchList(self):
        instance = ht_match.HattrickMatch()
        filePath = '2018/10/17/match.html'
        result = instance.findMatchList(filePath, 'mydatabase', 'player_tmp')
        print(filePath)
        for match in result:
            print(match)

    def test_findMatchList_2019_03_31(self):
        instance = ht_match.HattrickMatch()
        filePath = '2019/03/31/match.html'
        result = instance.findMatchList(filePath, 'mydatabase2', 'player_tmp')
        print(filePath)
        for match in result:
            print(match)

    def test_findMatchList_2019_04_03(self):
        instance = ht_match.HattrickMatch()
        filePath = '2019/04/03/match.html'
        result = instance.findMatchList(filePath, 'mydatabase', 'player_tmp')
        print(filePath)
        for match in result:
            print(match)

    """
    Test match_dict_list to match_str_list on mydatabase
    """
    def test_match_dict_list_to_match_str_list(self):
        instance = ht_match.HattrickMatch()
        filePath = '2018/04/18/match.html'
        match_dict_list = instance.findMatchList(filePath, 'mydatabase')
        match_str_list = instance.matchDictListToMatchStrList(match_dict_list)
        for str_line in match_str_list:
            print(str_line)
    """
    Test Away matchList
    """
    def test_away_findMatchList(self):
        instance = ht_match.HattrickMatch()
        filePath = '2018/10/17/match.html'
        result = instance.findMatchList(filePath, 'mydatabase', 'player_tmp')
        print(filePath)
        for match in result:
            print(match)

    def test_findMatchList_2019_03_31(self):
        instance = ht_match.HattrickMatch()
        filePath = '2019/03/31/match.html'
        result = instance.findMatchList(filePath, 'mydatabase2', 'player_tmp')
        print(filePath)
        for match in result:
            print(match)

    def test_findMatchList_2019_04_03(self):
        instance = ht_match.HattrickMatch()
        filePath = '2019/04/03/match.html'
        result = instance.findMatchList(filePath, 'mydatabase', 'player_tmp')
        print(filePath)
        for match in result:
            print(match)

    """
    Test match_dict_list to match_str_list on mydatabase
    """
    def test_match_dict_list_to_match_str_list(self):
        instance = ht_match.HattrickMatch()
        filePath = '2018/04/18/match.html'
        match_dict_list = instance.findMatchList(filePath, 'mydatabase')
        match_str_list = instance.matchDictListToMatchStrList(match_dict_list)
        for str_line in match_str_list:
            print(str_line)

    """
    Test match_dict_list to match_str_list on mydatabase2
    """
    def test_match_dict_list_to_match_str_list(self):
        instance = ht_match.HattrickMatch()
        filePath = '2018/05/09/match.html'
        match_dict_list = instance.findMatchList(filePath, 'mydatabase2')
        match_str_list = instance.matchDictListToMatchStrList(match_dict_list)
        for str_line in match_str_list:
            print(str_line)
