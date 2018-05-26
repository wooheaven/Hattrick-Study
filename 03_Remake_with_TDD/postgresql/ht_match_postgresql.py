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