import re
import pandas as pd
import json
import psycopg2
import copy

from bs4 import BeautifulSoup


class HattrickMatch():
    def isHome(self, homeTeamId):
        isHome = False
        if 1944941 == homeTeamId:
            print("LastKeeper HomeTeam")
            isHome = True
        elif 1949344 == homeTeamId:
            print("HeavyDefence HomeTeam")
            isHome = True
        return isHome

    def findMatchList(self, filePath, db_name, table_name):
        with open(filePath, 'r') as file:
            for idx, line in enumerate(file.readlines()):
                if "window.HT.ngMatch.data =" in line:
                    valueString = re.sub("window.HT.ngMatch.data = ", "", line.strip())
                    print('line num', idx, 'head 100', valueString[:100])
                    match_dict = json.loads(valueString)
                    break
        if 'homeTeamId' not in match_dict.keys():
            raise NotImplementedError('homeTeamID is not exists')
        homeTeamId = match_dict['homeTeamId']
        isHome = self.isHome(homeTeamId)
        if isHome:
            teamId = homeTeamId
        else:
            teamId = match_dict['awayTeamId']
        match_player = []
        for player in match_dict['players']:
            if teamId == player['teamId']:
                if 'sourcePlayerId' in player:
                    del player['sourcePlayerId']
                    del player['nickName']
                    del player['teamId']
                    del player['avatar']
                    del player['firstName']
                    del player['lastName']
                match_player.append(player)
        for event in match_dict['events']:
            if teamId == event['subjectTeamId']:
                # 21 starting lineup Player
                if 21 == event['eventType']:
                    p = re.compile('\d+\d')
                    for start_player_str in p.findall(event['eventText']):
                        self.set_sMin(int(start_player_str), 0, match_player)
                # 351,352 changing lineup Player
                elif 351 <= event['eventType'] <= 352:
                    start_player_num = int(event['subjectPlayerId'])
                    self.set_eMin(start_player_num, event['matchMinute'], match_player)
                    self.set_sMin(int(event['objectPlayerId']), event['matchMinute'], match_player, start_player_num)
            # 599 End of match
            elif 599 == event['eventType']:
                 for player in match_player:
                     if 'sMin' in player.keys() and 'eMin' not in player.keys():
                         self.set_eMin(int(player['playerId']), event['matchMinute'], match_player)
        match_avg = match_dict['analysis']['avg']
        for avg_player in (match_avg['homePlayers'] if isHome else match_avg['awayPlayers']):
            self.set_rt_po(int(avg_player['playerId']), avg_player['stars'], avg_player['positionId'], match_player)
        for player in match_player:
            if 'po_before' in player.keys():
                playerId = player['po_before']
                po = player['po']
                self.update_po(playerId, po, match_player)

        # soup = None
        # with open(filePath, 'r') as file:
        #     soup = BeautifulSoup(file.read(), "html.parser")
        #
        # div_id = "ctl00_ctl00_CPContent_CPMain_ucPostMatch_sectorAvgPanel"
        # if (isHome):
        #     print('Home')
        #     # input_id = 'ctl00_ctl00_CPContent_CPMain_ucPostMatch_rptTimeline_ctl14_playerRatingsHome'
        #     input_id = 'ctl00_ctl00_CPContent_CPMain_ucPostMatch_playerRatingsHome'
        # else:
        #     print('Away')
        #     # input_id = 'ctl00_ctl00_CPContent_CPMain_ucPostMatch_rptTimeline_ctl14_playerRatingsAway'
        #     input_id = 'ctl00_ctl00_CPContent_CPMain_ucPostMatch_playerRatingsAway'
        #
        # valueString = soup \
        #     .find_all("div", id=div_id)[0] \
        #     .find_all("input", id=input_id)[0] \
        #     .get('value')
        # match_dict = json.loads(valueString)
        #
        # # remove unUsedDictKeys
        # for index in range(len(match_dict)):
        #     match_dict[index].pop('PositionBehaviour', None)
        #     match_dict[index].pop('InjuryLevel', None)
        #     match_dict[index].pop('Stamina', None)
        #     match_dict[index].pop('Cards', None)
        #     match_dict[index].pop('IsCaptain', None)
        #     match_dict[index].pop('IsKicker', None)
        #
        # # remove PositionID 0, 114, 116, 117, 118, 120
        # removeList = list()
        # for index in range(0, len(match_dict)):
        #     position_id = match_dict[index]['PositionID']
        #     if (position_id == 0
        #             or position_id == 114
        #             or position_id == 115
        #             or position_id == 116
        #             or position_id == 117
        #             or position_id == 118
        #             or position_id == 119
        #             or position_id == 120):
        #         removeList.append(index)
        # for index in reversed(removeList):
        #     match_dict.pop(index)
        #
        # # change PositionID
        # for index in range(0, len(match_dict)):
        #     position_id = match_dict[index]['PositionID']
        #     if (position_id == 100):
        #         match_dict[index]['PositionID'] = 'KP'
        #         continue
        #     if (position_id == 101 or position_id == 105):
        #         match_dict[index]['PositionID'] = 'WB'
        #         continue
        #     if (position_id == 102 or position_id == 103 or position_id == 104):
        #         match_dict[index]['PositionID'] = 'CD'
        #         continue
        #     if (position_id == 106 or position_id == 110):
        #         match_dict[index]['PositionID'] = 'W'
        #         continue
        #     if (position_id == 107 or position_id == 108 or position_id == 109):
        #         match_dict[index]['PositionID'] = 'IM'
        #         continue
        #     if (position_id == 111 or position_id == 112 or position_id == 113):
        #         match_dict[index]['PositionID'] = 'FW'
        #         continue
        #     if (position_id == -1):
        #         date_str = filePath[:10]
        #         match_dict[index]['PositionID'] = \
        #             self.selectPOWherePlayerID(match_dict[index]['PlayerId'], date_str, db_name, table_name)
        #         continue
        #
        # # change FromMin
        # for index in range(0, len(match_dict)):
        #     from_min = match_dict[index]['FromMin']
        #     to_min = match_dict[index]['ToMin']
        #     if (from_min == -1):
        #         match_dict[index]['FromMin'] = 0
        #     if (91 <= to_min  <= 94):
        #         match_dict[index]['ToMin'] = 90
        #
        # # find PlayerNum
        # for index in range(0, len(match_dict)):
        #     match_dict[index]['PlayerNum'] = self.selectPlayerNumWherePlayerId(match_dict[index]['PlayerId'],
        #                                                                             db_name,
        #                                                                             table_name)
        #
        # # sort by PositionID
        # def PositionID_key_sort_func(single_player):
        #     if single_player['PositionID'] == 'KP':
        #         return (1, single_player['FromMin'], -single_player['ToMin'])
        #     elif single_player['PositionID'] == 'WB':
        #         return (2, single_player['FromMin'], -single_player['ToMin'])
        #     elif single_player['PositionID'] == 'CD':
        #         return (3, single_player['FromMin'], -single_player['ToMin'])
        #     elif single_player['PositionID'] == 'W':
        #         return (4, single_player['FromMin'], -single_player['ToMin'])
        #     elif single_player['PositionID'] == 'IM':
        #         return (5, single_player['FromMin'], -single_player['ToMin'])
        #     elif single_player['PositionID'] == 'FW':
        #         return (6, single_player['FromMin'], -single_player['ToMin'])
        #     else:
        #         return (7, single_player['FromMin'], -single_player['ToMin'])
        # match_dict.sort(key=PositionID_key_sort_func)
        #
        # # find and update Stars = -1.0
        # for index in range(len(match_dict)):
        #     starts = match_dict[index]['Stars']
        #     if (starts == -1.0):
        #         date_str = filePath[:10]
        #         playerid = match_dict[index]['PlayerId']
        #         match_dict[index]['Stars'] = self.selectRTWhereDateAndPlayerId(date_str,
        #                                                                             playerid,
        #                                                                             db_name,
        #                                                                             table_name)
        #
        # return match_dict
        for idx,player in enumerate(match_player):
            if 'po_before' in player.keys():
                if player['po_before'] == match_player[idx+1]['playerId']:
                    tmp_player = copy.deepcopy(player)
                    match_player[idx] = match_player[idx+1]
                    match_player[idx+1] = tmp_player
        print('po,num,rt,sMin,eMin')
        for player in match_player:
            if 'po' in player.keys():
                print(str(player['po'])+','+str(player['playerNumber'])+','+str(player['rt'])+','+str(player['sMin'])+','+str(player['eMin']))
        return match_player

    def set_sMin(self, playerId, sMin, match_player, start_player_num=-1):
        for player in match_player:
            if playerId == player['playerId']:
                player['sMin'] = sMin
                if start_player_num > -1:
                    player['po_before'] = start_player_num
                break

    def set_eMin(self, playerId, eMin, match_player):
        for player in match_player:
            if playerId == player['playerId']:
                player['eMin'] = eMin
                break

    def set_rt_po(self, playerId, rt, po, match_player):
        if 100 == po:
            po = 'KP'
        elif 101 == po or 105 == po:
            po = 'WB'
        elif 102 <= po <= 104:
            po = 'CD'
        elif 106 == po or 110 == po:
            po = 'W'
        elif 107 <= po <= 109:
            po = 'IM'
        elif 111 <= po <= 113:
            po = 'FW'
        for player in match_player:
            if playerId == player['playerId'] and 'sMin' in player.keys() and 'eMin' in player.keys():
                player['rt'] = rt
                player['po'] = po
                break

    def update_po(self, playerId, po, match_player):
        for player in match_player:
            if playerId == player['playerId']:
                player['po'] = po
                break

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
        current_conn = None
        try:
            current_conn = psycopg2.connect(\
                'dbname=' + db_name + ' user=myuser host=localhost port=65432 password=123qwe')
            current_sql = 'SELECT num FROM ' + table_name + ' WHERE playerid = ' + str(PlayerId) + ' LIMIT 1'
            df = pd.read_sql(sql=current_sql, con=current_conn)
            # print(df)
        except (Exception, psycopg2.DatabaseError) as errors:
            print(current_sql)
            print(errors)
        finally:
            if current_conn is not None:
                current_conn.close()
        return df['num'][0]

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
