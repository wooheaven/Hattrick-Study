import json
import psycopg2

from bs4 import BeautifulSoup

class HattrickMatch():
    def findMatchList(self, filePath, db_name):
        with open(filePath, 'r') as file:
            soup = BeautifulSoup(file.read(), "html.parser")
            valueString = soup \
                            .find_all("div", id="ctl00_ctl00_CPContent_CPMain_ucPostMatch_rptTimeline_ctl14_timelineEventPanel")[0] \
                            .find_all("input", id="ctl00_ctl00_CPContent_CPMain_ucPostMatch_rptTimeline_ctl14_playerRatingsHome")[0] \
                            .get('value')
            player_dict = json.loads(valueString)

            # remove PositionID 0, 114, 117, 118, 120
            removeList = list()
            for index in range(0, len(player_dict)):
                position_id = player_dict[index]['PositionID']
                if (position_id == 0 or position_id == 114 or position_id == 117 or position_id == 118 or position_id == 120):
                    removeList.append(index)
            for index in reversed(removeList):
                player_dict.pop(index)

            # change PositionID
            for index in range(0, len(player_dict)):
                position_id = player_dict[index]['PositionID']
                if (position_id == 100):
                    player_dict[index]['PositionID'] = 'KP'
                    continue
                if (position_id == 101 or position_id == 105):
                    player_dict[index]['PositionID'] = 'WB'
                    continue
                if (position_id == 102 or position_id == 103 or position_id == 104):
                    player_dict[index]['PositionID'] = 'CD'
                    continue
                if (position_id == 106 or position_id == 110):
                    player_dict[index]['PositionID'] = 'W'
                    continue
                if (position_id == 107 or position_id == 108 or position_id == 109):
                    player_dict[index]['PositionID'] = 'IM'
                    continue
                if (position_id == 111 or position_id == 112 or position_id == 113):
                    player_dict[index]['PositionID'] = 'FW'
                    continue
                if (position_id == -1):
                    player_dict[index]['PositionID'] = \
                        self.selectPOWherePlayerID(player_dict[index]['PlayerId'], db_name)
                    continue
        return player_dict

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
