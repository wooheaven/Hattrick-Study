import re
import pandas as pd
import json
import psycopg2
import copy


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
        match_dict = dict()
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
                # 512 red card Player
                elif 512 == event['eventType']:
                    p = re.compile('player=\d+\d')
                    for red_card_player_str_tmp in p.findall(event['eventText']):
                        p = re.compile('\d+\d')
                        for red_card_player_str in p.findall(red_card_player_str_tmp):
                            self.set_eMin(int(red_card_player_str), int(event['matchMinute']), match_player)
                # 351,352 changing lineup Player
                elif 351 <= event['eventType'] <= 352:
                    start_player_num = int(event['subjectPlayerId'])
                    self.set_eMin(start_player_num, event['matchMinute'], match_player)
                    self.set_sMin(int(event['objectPlayerId']), event['matchMinute'], match_player, start_player_num)
            elif 501 == event['eventType']:
                 for player in match_player:
                     if 'sMin' in player.keys() and 'eMin' not in player.keys():
                         self.set_eMin(int(player['playerId']), 0, match_player)
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
        for idx,player in enumerate(match_player):
            if 'po_before' in player.keys():
                if player['po_before'] == match_player[idx+1]['playerId']:
                    tmp_player = copy.deepcopy(player)
                    match_player[idx] = match_player[idx+1]
                    match_player[idx+1] = tmp_player
        # update player's po whose po is -1
        for player in match_player:
            if 'po' in player.keys():
                if player['po'] == -1:
                    p = re.compile('\d\d\d\d-\d\d-\d\d')
                    for date_str in p.findall(match_dict['matchDate']):
                        po = self.selectPOWherePlayerID(player['playerId'], date_str, db_name, table_name)
                        self.update_po(player['playerId'], po, match_player)
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

    def print_match_player(self, match_player):
        print('po,num,rt,sMin,eMin')
        for player in match_player:
            if 'po' in player.keys():
                print(str(player['po'])+','+str(player['playerNumber'])+','+str(player['rt'])+','+str(player['sMin'])+','+str(player['eMin']))

    def save_match_player(self, file_path, match_player):
        with open(file_path, 'w') as f:
            f.write('po,num,rt,sMin,eMin\n')
            for player in match_player:
                if 'po' in player.keys():
                    f.write(str(player['po'])+','+str(player['playerNumber'])+','+str(player['rt'])+','+str(player['sMin'])+','+str(player['eMin'])+'\n')

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
