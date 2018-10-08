import json
import psycopg2

from bs4 import BeautifulSoup


class HattrickMatch():
    def isHome(self, filePath, db_name, table_name):
        soup = None
        with open(filePath, 'r') as file:
            soup = BeautifulSoup(file.read(), "html.parser")

        div_id = "ctl00_ctl00_CPContent_CPMain_ucPostMatch_rptTimeline_ctl14_timelineEventPanel"
        input_id = "ctl00_ctl00_CPContent_CPMain_ucPostMatch_rptTimeline_ctl14_playerRatingsHome"
        valueString = soup \
            .find_all("div", id=div_id)[0] \
            .find_all("input", id=input_id)[0] \
            .get('value')
        match_dict_list = json.loads(valueString)

        kp_player_id = None
        for index in range(len(match_dict_list)):
            if (match_dict_list[index]['PositionID'] == 100):
                kp_player_id = match_dict_list[index]['PlayerId']
                break

        kp_player_count = 0
        kp_player_count = self.selectCountOfWherePlayerID(kp_player_id, db_name, table_name)
        return (kp_player_count > 0)

    def findMatchList(self, filePath, db_name, table_name):
        isHome = None
        isHome = self.isHome(filePath, db_name, table_name)

        soup = None
        with open(filePath, 'r') as file:
            soup = BeautifulSoup(file.read(), "html.parser")

        div_id = "ctl00_ctl00_CPContent_CPMain_ucPostMatch_rptTimeline_ctl14_timelineEventPanel"
        if (isHome):
            print('Home')
            input_id = 'ctl00_ctl00_CPContent_CPMain_ucPostMatch_rptTimeline_ctl14_playerRatingsHome'
        else:
            print('Away')
            input_id = 'ctl00_ctl00_CPContent_CPMain_ucPostMatch_rptTimeline_ctl14_playerRatingsAway'

        valueString = soup \
            .find_all("div", id=div_id)[0] \
            .find_all("input", id=input_id)[0] \
            .get('value')
        match_dict_list = json.loads(valueString)

        # remove unUsedDictKeys
        for index in range(len(match_dict_list)):
            match_dict_list[index].pop('PositionBehaviour', None)
            match_dict_list[index].pop('InjuryLevel', None)
            match_dict_list[index].pop('Stamina', None)
            match_dict_list[index].pop('Cards', None)
            match_dict_list[index].pop('IsCaptain', None)
            match_dict_list[index].pop('IsKicker', None)

        # remove PositionID 0, 114, 116, 117, 118, 120
        removeList = list()
        for index in range(0, len(match_dict_list)):
            position_id = match_dict_list[index]['PositionID']
            if (position_id == 0
                    or position_id == 114
                    or position_id == 115
                    or position_id == 116
                    or position_id == 117
                    or position_id == 118
                    or position_id == 119
                    or position_id == 120):
                removeList.append(index)
        for index in reversed(removeList):
            match_dict_list.pop(index)

        # change PositionID
        for index in range(0, len(match_dict_list)):
            position_id = match_dict_list[index]['PositionID']
            if (position_id == 100):
                match_dict_list[index]['PositionID'] = 'KP'
                continue
            if (position_id == 101 or position_id == 105):
                match_dict_list[index]['PositionID'] = 'WB'
                continue
            if (position_id == 102 or position_id == 103 or position_id == 104):
                match_dict_list[index]['PositionID'] = 'CD'
                continue
            if (position_id == 106 or position_id == 110):
                match_dict_list[index]['PositionID'] = 'W'
                continue
            if (position_id == 107 or position_id == 108 or position_id == 109):
                match_dict_list[index]['PositionID'] = 'IM'
                continue
            if (position_id == 111 or position_id == 112 or position_id == 113):
                match_dict_list[index]['PositionID'] = 'FW'
                continue
            if (position_id == -1):
                date_str = filePath[:10]
                match_dict_list[index]['PositionID'] = \
                    self.selectPOWherePlayerID(match_dict_list[index]['PlayerId'], date_str, db_name, table_name)
                continue

        # change FromMin
        for index in range(0, len(match_dict_list)):
            from_min = match_dict_list[index]['FromMin']
            to_min = match_dict_list[index]['ToMin']
            if (from_min == -1):
                match_dict_list[index]['FromMin'] = 0
            if (91 <= to_min  <= 94):
                match_dict_list[index]['ToMin'] = 90

        # find PlayerNum
        for index in range(0, len(match_dict_list)):
            match_dict_list[index]['PlayerNum'] = self.selectPlayerNumWherePlayerId(match_dict_list[index]['PlayerId'],
                                                                                    db_name,
                                                                                    table_name)

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
        match_dict_list.sort(key=PositionID_key_sort_func)

        # find and update Stars = -1.0
        for index in range(len(match_dict_list)):
            starts = match_dict_list[index]['Stars']
            if (starts == -1.0):
                date_str = filePath[:10]
                playerid = match_dict_list[index]['PlayerId']
                match_dict_list[index]['Stars'] = self.selectRTWhereDateAndPlayerId(date_str,
                                                                                    playerid,
                                                                                    db_name,
                                                                                    table_name)

        return match_dict_list

    def selectPOWherePlayerID(self, player_id, date_str, db_name, table_name):
        conn = None
        try:
            conn = psycopg2.connect(\
                'dbname=' + db_name + ' user=myuser host=localhost port=65432 password=123qwe')
            sql = ''
            sql += 'SELECT po '
            sql += 'FROM ' + table_name + ' '
            sql += 'WHERE playerid = ' + str(player_id) + ' AND date=\'' + date_str + '\''
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

    def selectPlayerNumWherePlayerId(self, PlayerId, db_name, table_name):
        conn = None
        try:
            conn = psycopg2.connect(\
                'dbname=' + db_name + ' user=myuser host=localhost port=65432 password=123qwe')
            sql = 'SELECT num FROM ' + table_name + ' WHERE playerid =' + str(PlayerId) + ' LIMIT 1'
            cur = conn.cursor()
            cur.execute(sql)
            row = cur.fetchone()
        except (Exception, psycopg2.DatabaseError) as errors:
            print(sql)
            print(errors)
        finally:
            if conn is not None:
                conn.close()
        return row[0]

    def selectCountOfWherePlayerID(self, PlayerId, db_name, table_name):
        conn = None
        try:
            conn = psycopg2.connect('dbname=' + db_name + ' user=myuser host=localhost port=65432 password=123qwe')
            sql = 'SELECT COUNT(playerid) FROM ' + table_name + ' WHERE playerid =' + str(PlayerId)
            cur = conn.cursor()
            cur.execute(sql)
            row = cur.fetchone()
        except (Exception, psycopg2.DatabaseError) as errors:
            print(errors)
        finally:
            if conn is not None:
                conn.close()
        return row[0]

    def matchDictListToMatchStrList(self, match_dict_list):
        match_str_list = ['po,num,rt,sMin,eMin']
        po_str = ''
        num_str = ''
        rt_str = ''
        sMin = ''
        eMin = ''
        str_line = ''
        for index in range(len(match_dict_list)):
            po_str = str(match_dict_list[index]['PositionID'])
            num_str = str(match_dict_list[index]['PlayerNum'])
            rt_str = str(match_dict_list[index]['Stars'])
            sMin = str(match_dict_list[index]['FromMin'])
            eMin = str(match_dict_list[index]['ToMin'])
            str_line = po_str
            str_line += ',' + num_str
            str_line += ',' + rt_str
            str_line += ',' + sMin
            str_line += ',' + eMin
            match_str_list.append(str_line)
        return match_str_list

    def selectRTWhereDateAndPlayerId(self, date_str, playerid, db_name, table_name):
        conn = None
        try:
            conn = psycopg2.connect( \
                'dbname=' + db_name + ' user=myuser host=localhost port=65432 password=123qwe')
            sql = 'SELECT rt FROM ' + table_name + ' WHERE playerid =' + str(playerid) + ' AND date =\'' + date_str + '\''
            cur = conn.cursor()
            cur.execute(sql)
            row = cur.fetchone()
        except (Exception, psycopg2.DatabaseError) as errors:
            print(errors)
        finally:
            if conn is not None:
                conn.close()
        return float(row[0])
