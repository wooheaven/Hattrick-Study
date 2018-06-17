import psycopg2


class HattrickMatchPostgreSQL():
    def getMatchByPoNum(self, conn, po, numList):
        tupleList = list();
        query = None
        try:
            cur = conn.cursor()
            query =  """SELECT * """                                                        + "\n"
            query += """FROM crosstab( """                                                  + "\n"
            query += """    'SELECT """                                                     + "\n"
            query += """        date, """                                                   + "\n"
            query += """        num, """                                                    + "\n"
            query += """        CASE """                                                    + "\n"
            query += """            WHEN length(time_rt)=5 THEN ''  ''||''''||time_rt """   + "\n"
            query += """            WHEN length(time_rt)=6 THEN '' ''||''''||time_rt """    + "\n"
            query += """            WHEN length(time_rt)=7 THEN time_rt """                 + "\n"
            query += """            ELSE ''error'' """                                      + "\n"
            query += """        END AS time_rt """                                          + "\n"
            query += """    FROM ( """                                                      + "\n"
            query += """        SELECT """                                                  + "\n"
            query += """            date :: VARCHAR(10), """                                + "\n"
            query += """            num :: VARCHAR(2), """                                  + "\n"
            query += """            emin-smin||''/''||rt :: VARCHAR(7) as time_rt """       + "\n"
            query += """        FROM match """                                              + "\n"
            query += """        WHERE """                                                   + "\n"
            query += """            po = ''PO'' and current_date - 30 < date """            + "\n"
            query += """        ORDER BY """                                                + "\n"
            query += """            date, num """                                           + "\n"
            query += """    ) AS a', """                                                    + "\n"
            query += """    'SELECT m from unnest(''{numListStr}''::int[]) m' """           + "\n"
            query += """) """                                                               + "\n"
            query += """AS ( """                                                            + "\n"
            query += """    "date num min/rt" VARCHAR(10), """                              + "\n"
            query += """numColumnStr """                                                    + "\n"
            query += """) """                                                               + "\n"
            query += """ORDER BY 1 """                                                      + "\n"

            query = query.replace("PO", po, 1)
            numListStr = str(numList[0])
            for index in range(1, len(numList)):
                numListStr += "," + str(numList[index])
            query = query.replace("numListStr", numListStr, 1)
            numColumnStr = ""
            for index in range(len(numList)-1):
                numColumnStr += "    \"   " + str(numList[index]) + "  \" VARCHAR(8)," + "\n"
            numColumnStr += "    \"   " + str(numList[len(numList)-1]) + "  \" VARCHAR(8) "
            query = query.replace("numColumnStr", numColumnStr, 1)

            # print(query)
            cur.execute(query)
            row = cur.fetchone()
            while row is not None:
                tupleList.append(row)
                row = cur.fetchone()
        except (Exception, psycopg2.DatabaseError) as error:
            print(query)
            print("Error Happend")
            print(error)
        return tupleList

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
        return tuple_list

    def printMatchByPoNum(self, tupleList, numList):
        headStr = "date num min/rt |"
        for num in numList:
            numStr = str(num)
            if len(numStr) == 1:
               numStr = "0" + numStr
            headStr += "    " + numStr + "   |"
        print(headStr)

        rowLineStr = "----------------|"
        for index in range(len(numList)):
            rowLineStr += "---------|"
        print(rowLineStr)

        for tuple in tupleList:
            lineStr = str(tuple[0]) + "      |"
            for index in range(1, len(tuple)):
                lineStr += self.convertToStr(tuple[index])
            print(lineStr)

    def convertToStr(self, column):
        if column is None:
            return "         |"
        else:
            return " " + str(column) + " |"

    def printMatchByDate(self, tuple_list):
        for tuple in tuple_list:
            line_str = str(tuple[0])
            for index in range(1, len(tuple)):
                line_str += "\t" + str(tuple[index])
            print(line_str)