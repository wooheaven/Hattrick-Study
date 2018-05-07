import json
import psycopg2

from bs4 import BeautifulSoup

class HattrickMatch():
    def isHome(self, filePath, db_name):
        soup = None
        with open(filePath, 'r') as file:
            soup = BeautifulSoup(file.read(), "html.parser")

        div_id = "ctl00_ctl00_CPContent_CPMain_ucPostMatch_rptTimeline_ctl14_timelineEventPanel"
        input_id = "ctl00_ctl00_CPContent_CPMain_ucPostMatch_rptTimeline_ctl14_playerRatingsHome"
        valueString = soup \
            .find_all("div", id=div_id)[0] \
            .find_all("input", id=input_id)[0] \
            .get('value')
        player_dict_list = json.loads(valueString)

        kp_player_id = None
        for index in range(len(player_dict_list)):
            if (player_dict_list[index]['PositionID'] == 100):
                kp_player_id = player_dict_list[index]['PlayerId']
                break

        kp_player_count = 0
        kp_player_count = self.selectCountOfWherePlayerID(kp_player_id, db_name)
        return (kp_player_count > 0)

    def findMatchList(self, filePath, db_name):
        isHome = None
        isHome = self.isHome(filePath, db_name)

        soup = None
        with open(filePath, 'r') as file:
            soup = BeautifulSoup(file.read(), "html.parser")

        div_id = "ctl00_ctl00_CPContent_CPMain_ucPostMatch_rptTimeline_ctl14_timelineEventPanel"
        if (isHome):
            input_id = 'ctl00_ctl00_CPContent_CPMain_ucPostMatch_rptTimeline_ctl14_playerRatingsHome'
        else:
            input_id = 'ctl00_ctl00_CPContent_CPMain_ucPostMatch_rptTimeline_ctl14_playerRatingsAway'

        valueString = soup \
            .find_all("div", id=div_id)[0] \
            .find_all("input", id=input_id)[0] \
            .get('value')
        player_dict_list = json.loads(valueString)

        # remove unUsedDictKeys
        for index in range(len(player_dict_list)):
            player_dict_list[index].pop('PositionBehaviour', None)
            player_dict_list[index].pop('InjuryLevel', None)
            player_dict_list[index].pop('Stamina', None)
            player_dict_list[index].pop('Cards', None)
            player_dict_list[index].pop('IsCaptain', None)
            player_dict_list[index].pop('IsKicker', None)

        # remove PositionID 0, 114, 117, 118, 120
        removeList = list()
        for index in range(0, len(player_dict_list)):
            position_id = player_dict_list[index]['PositionID']
            if (position_id == 0 or position_id == 114 or position_id == 117 or position_id == 118 or position_id == 120):
                removeList.append(index)
        for index in reversed(removeList):
            player_dict_list.pop(index)

        # change PositionID
        for index in range(0, len(player_dict_list)):
            position_id = player_dict_list[index]['PositionID']
            if (position_id == 100):
                player_dict_list[index]['PositionID'] = 'KP'
                continue
            if (position_id == 101 or position_id == 105):
                player_dict_list[index]['PositionID'] = 'WB'
                continue
            if (position_id == 102 or position_id == 103 or position_id == 104):
                player_dict_list[index]['PositionID'] = 'CD'
                continue
            if (position_id == 106 or position_id == 110):
                player_dict_list[index]['PositionID'] = 'W'
                continue
            if (position_id == 107 or position_id == 108 or position_id == 109):
                player_dict_list[index]['PositionID'] = 'IM'
                continue
            if (position_id == 111 or position_id == 112 or position_id == 113):
                player_dict_list[index]['PositionID'] = 'FW'
                continue
            if (position_id == -1):
                player_dict_list[index]['PositionID'] = \
                    self.selectPOWherePlayerID(player_dict_list[index]['PlayerId'], db_name)
                continue

        # change FromMin
        for index in range(0, len(player_dict_list)):
            from_min = player_dict_list[index]['FromMin']
            to_min = player_dict_list[index]['ToMin']
            if (from_min == -1):
                player_dict_list[index]['FromMin'] = 0
            if (91 <= to_min  <= 94):
                player_dict_list[index]['FromMin'] = 90

        # find PlayerNum
        for index in range(0, len(player_dict_list)):
            player_dict_list[index]['PlayerNum'] = self.selectPlayerNumWherePlayerId(player_dict_list[index]['PlayerId'], db_name)

        # sort by PositionID
        def PositionID_key_sort_func(single_player):
            if single_player['PositionID'] == 'KP':
                return (1, single_player['FromMin'], -single_player['ToMin'])
            elif single_player['PositionID'] == 'WB':
                return (2, single_player['FromMin'], -single_player['ToMin'])
            elif single_player['PositionID'] == 'CD':
                return (3, single_player['FromMin'], -single_player['ToMin'])
            elif single_player['PositionID'] == 'W':
                return (4, single_player['FromMin'], -single_player['ToMin'])
            elif single_player['PositionID'] == 'IM':
                return (5, single_player['FromMin'], -single_player['ToMin'])
            elif single_player['PositionID'] == 'FW':
                return (6, single_player['FromMin'], -single_player['ToMin'])
            else:
                return (7, single_player['FromMin'], -single_player['ToMin'])
        player_dict_list.sort(key=PositionID_key_sort_func)

        return player_dict_list

    def selectPOWherePlayerID(self, player_id, db_name):
        conn = None
        try:
            conn = psycopg2.connect(\
                'dbname=' + db_name + ' user=myuser host=localhost port=65432 password=123qwe')
            sql = 'SELECT po FROM player WHERE playerid =' + str(player_id) + ' LIMIT 1'
            cur = conn.cursor()
            cur.execute(sql)
            row = cur.fetchone()
        except (Exception, psycopg2.DatabaseError) as errors:
            print(errors)
            # print(sql)
        finally:
            if conn is not None:
                conn.close()
        return row[0]

    def selectPlayerNumWherePlayerId(self, PlayerId, db_name):
        conn = None
        try:
            conn = psycopg2.connect(\
                'dbname=' + db_name + ' user=myuser host=localhost port=65432 password=123qwe')
            sql = 'SELECT num FROM player WHERE playerid =' + str(PlayerId) + ' LIMIT 1'
            cur = conn.cursor()
            cur.execute(sql)
            row = cur.fetchone()
        except (Exception, psycopg2.DatabaseError) as errors:
            print(errors)
        finally:
            if conn is not None:
                conn.close()
        return row[0]

    def selectCountOfWherePlayerID(self, PlayerId, db_name):
        conn = None
        try:
            conn = psycopg2.connect( \
                'dbname=' + db_name + ' user=myuser host=localhost port=65432 password=123qwe')
            sql = 'SELECT COUNT(playerid) FROM player WHERE playerid =' + str(PlayerId)
            cur = conn.cursor()
            cur.execute(sql)
            row = cur.fetchone()
        except (Exception, psycopg2.DatabaseError) as errors:
            print(errors)
        finally:
            if conn is not None:
                conn.close()
        return row[0]