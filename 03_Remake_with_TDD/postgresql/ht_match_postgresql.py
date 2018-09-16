import psycopg2


class HattrickMatchPostgreSQL():

    def select_count_of_match(self, conn):
        try:
            cur = conn.cursor()
            sql = "SELECT COUNT(*) FROM match"
            cur.execute(sql)
            row = cur.fetchone()
            count = row[0]
            return count
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error Happend")
            print(error)
            print(sql)
        finally:
            if cur is not None:
                cur.close()

    def insert_to_match(self, conn, time, row):
        try:
            cur = conn.cursor()
            sql = ""
            sql += "INSERT INTO match (                                                   " + "\n"
            sql += "    date,                          -- 02                              " + "\n"
            sql += "    po,                            -- 03                              " + "\n"
            sql += "    num,                           -- 04                              " + "\n"
            sql += "    rt,                            -- 05                              " + "\n"
            sql += "    smin,                          -- 06                              " + "\n"
            sql += "    emin                           -- 07                              " + "\n"
            sql += ") (                                                                   " + "\n"
            sql += "    SELECT                                                            " + "\n"
            sql += "        to_date(%s, 'YYYY-MM-DD'), -- 02 date DATE          Date      " + "\n"
            sql += "        %s,                        -- 03 po   VARCHAR(5)    Position  " + "\n"
            sql += "        %s,                        -- 04 num  INT           Number    " + "\n"
            sql += "        %s,                        -- 05 rt   NUMERIC(2, 1) Rating    " + "\n"
            sql += "        %s,                        -- 06 sMin INT           Start Min " + "\n"
            sql += "        %s                         -- 07 eMin INT           End Min   " + "\n"
            sql += ")                                                                     " + "\n"
            cur.execute(sql, (time, row[0], row[1], row[2], row[3], row[4]))
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error Happend")
            print(error)
            print(sql)
            print(row)
        finally:
            if cur is not None:
                cur.close()

    def update_rt_of_match(self, conn):
        try:
            cur = conn.cursor()
            sql = ""
            sql += "UPDATE match                      " + "\n"
            sql += "SET rt = p.rt                     " + "\n"
            sql += "FROM player_new AS p              " + "\n"
            sql += "    WHERE                         " + "\n"
            sql += "        match.date = p.date       " + "\n"
            sql += "            and p.date = p.last   " + "\n"
            sql += "            and match.po = p.po   " + "\n"
            sql += "            and match.num = p.num " + "\n"
            sql += "            and match.rt != p.rt  "
            cur.execute(sql)
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(sql)
            print("Error Happend")
            print(error)
        finally:
            if cur is not None:
                cur.close()

    def getMatchByPoNum(self, conn, po, num_list):
        tuple_list = list()
        query = None
        try:
            cur = conn.cursor()
            query = ""
            query += "SELECT *                                                      " + "\n"
            query += "FROM crosstab(                                                " + "\n"
            query += "    'SELECT                                                   " + "\n"
            query += "        date,                                                 " + "\n"
            query += "        num,                                                  " + "\n"
            query += "        CASE                                                  " + "\n"
            query += "            WHEN length(time_rt)=5 THEN ''  ''||''''||time_rt " + "\n"
            query += "            WHEN length(time_rt)=6 THEN '' ''||''''||time_rt  " + "\n"
            query += "            WHEN length(time_rt)=7 THEN time_rt               " + "\n"
            query += "            ELSE ''error''                                    " + "\n"
            query += "        END AS time_rt                                        " + "\n"
            query += "    FROM (                                                    " + "\n"
            query += "        SELECT                                                " + "\n"
            query += "            date :: VARCHAR(10),                              " + "\n"
            query += "            num :: VARCHAR(2),                                " + "\n"
            query += "            emin-smin||''/''||rt :: VARCHAR(7) as time_rt     " + "\n"
            query += "        FROM match                                            " + "\n"
            query += "        WHERE                                                 " + "\n"
            query += "            po = ''PO'' and current_date - 30 < date          " + "\n"
            query += "        ORDER BY                                              " + "\n"
            query += "            date, num                                         " + "\n"
            query += "    ) AS a',                                                  " + "\n"
            query += "    'SELECT m from unnest(''{numListStr}''::int[]) m'         " + "\n"
            query += ")                                                             " + "\n"
            query += "AS (                                                          " + "\n"
            query += "    \"date num min/rt\" VARCHAR(10),                          " + "\n"
            query += "    numColumnStr                                              " + "\n"
            query += ")                                                             " + "\n"
            query += "ORDER BY 1                                                    " + "\n"

            query = query.replace("PO", po, 1)
            num_list_str = str(num_list[0])
            for index in range(1, len(num_list)):
                num_list_str += "," + str(num_list[index])
            query = query.replace("numListStr", num_list_str, 1)
            num_column_str = ""
            for index in range(len(num_list) - 1):
                num_column_str += "    \"   " + str(num_list[index]) + "  \" VARCHAR(8)," + "\n"
            num_column_str += "    \"   " + str(num_list[len(num_list) - 1]) + "  \" VARCHAR(8) "
            query = query.replace("numColumnStr", num_column_str, 1)

            # print(query)
            cur.execute(query)
            row = cur.fetchone()
            while row is not None:
                tuple_list.append(row)
                row = cur.fetchone()
        except (Exception, psycopg2.DatabaseError) as error:
            print(query)
            print("Error Happend")
            print(error)
        finally:
            if cur is not None:
                cur.close()
        return tuple_list

    def getMatchByDate(self, date, conn):
        tuple_list = []
        query = ""
        try:
            cur = conn.cursor()
            query += "SELECT                                    " + "\n"
            query += "    po, num, rt :: VARCHAR(5), smin, emin " + "\n"
            query += "FROM                                      " + "\n"
            query += "    match                                 " + "\n"
            query += "WHERE                                     " + "\n"
            query += "    date ='" + date.replace('/', '-') + "'" + "\n"
            query += "ORDER BY                                  " + "\n"
            query += "    CASE                                  " + "\n"
            query += "        WHEN po = 'KP' THEN 1             " + "\n"
            query += "        WHEN po = 'WB' THEN 2             " + "\n"
            query += "        WHEN po = 'CD' THEN 3             " + "\n"
            query += "        WHEN po = 'W'  THEN 4             " + "\n"
            query += "        WHEN po = 'IM' THEN 5             " + "\n"
            query += "        WHEN po = 'FW' THEN 6             " + "\n"
            query += "        ELSE 7                            " + "\n"
            query += "    END,                                  " + "\n"
            query += "    emin asc, smin desc                   " + "\n"
            cur.execute(query)
            row = cur.fetchone()
            while row is not None:
                tuple_list.append(row)
                row = cur.fetchone()
        except (Exception, psycopg2.DatabaseError) as error:
            print(query)
            print("Error Happend")
            print(error)
        finally:
            if cur is not None:
                cur.close()
        return tuple_list

    def printMatchByPoNum(self, tupleList, numList):
        head_str = "date num min/rt |"
        for num in numList:
            numStr = str(num)
            if len(numStr) == 1:
               numStr = "0" + numStr
            head_str += "    " + numStr + "   |"
        print(head_str)

        row_line_str = "----------------|"
        for index in range(len(numList)):
            row_line_str += "---------|"
        print(row_line_str)

        for t in tupleList:
            line_str = str(t[0]) + "      |"
            for index in range(1, len(t)):
                line_str += self.convertToStr(t[index])
            print(line_str)

    def convertToStr(self, column):
        if column is None:
            return "         |"
        else:
            return " " + str(column) + " |"

    def printMatchByDate(self, tuple_list):
        for t in tuple_list:
            line_str = str(t[0])
            for index in range(1, len(t)):
                line_str += "\t" + str(t[index])
            print(line_str)
