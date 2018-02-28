import re
import psycopg2

def removeFirstChrLastChr(inputList):
    outputList = list();
    for line in inputList:
        line = line.replace("[", "", 1).replace("]", "", 1).replace("{", "", 1).replace("}", "", 1)
        outputList.append(line)
    return outputList

def filterColumn(inputList):
    outputList = list();
    for line in inputList:
        col = line.split(",")
        col[1] = re.sub('"PositionID":', '', col[1])
        col[0] = re.sub('"PlayerId":', '', col[0])
        col[3] = re.sub('"Stars":', '', col[3])
        col[9] = re.sub('"FromMin":', '', col[9])
        col[10] = re.sub('"ToMin":', '', col[10])
        
        newLine = col[1] + "," + col[0] + "," + col[3] + "," + col[9] + "," + col[10]
        outputList.append(newLine)
    return outputList

def renamePO(inputList, dbname):
    # PO(Position) 이 KP, WB, CD, W, IM, FW, -1(교체) 만 matchList에 남기기
    outputList = list();
    for line in inputList:
        enabled = False
        col = line.split(",")

        if ( col[0] == "100" ): 
            col[0] = "KP"
            enabled = True
        if ( col[0] == "101" or col[0] == "105" ):
            col[0] = "WB"
            enabled = True
        if ( col[0] == "102" or col[0] == "103" or col[0] == "104" ):
            col[0] = "CD"
            enabled = True
        if ( col[0] == "106" or col[0] == "110" ): 
            col[0] = "W"
            enabled = True
        if ( col[0] == "107" or col[0] == "108" or col[0] == "109" ):
            col[0] = "IM"
            enabled = True
        if ( col[0] == "111" or col[0] == "112" or col[0] == "113" ): 
            col[0] = "FW"
            enabled = True
        if ( col[0] == "-1" ):
            col[0] = selectPOByPlayerID(col[1], dbname)
            enabled = True

        if enabled:
            newLine = col[0] + "," + col[1] + "," + col[2] + "," + col[3] + "," + col[4]
            outputList.append(newLine)

    return outputList

def selectPOByPlayerID(playerId, dbname):
    outputList = list();
    conn = None
    try:
        conn = psycopg2.connect("dbname='" + dbname + "' user='myuser' host='localhost' port='65432' password='123qwe'")
        cur = conn.cursor()
        sql = "SELECT po FROM player WHERE playerid = '" + playerId + "' ORDER BY date DESC LIMIT 1"
        print(sql)
        cur.execute(sql)
        row = cur.fetchone()
        while row is not None:
            #print(row)
            outputList.append(row)
            row = cur.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        print(sql)
    finally:
        if conn is not None:
            conn.close()
    return outputList[0][0]

def renameMin(inputList):
    outputList = list();
    for line in inputList:
        col = line.split(",")
        if col[3] == "-1" : col[3] = "0"
        if col[4] == "-1" : col[4] = "0"
        if col[4] == "91" : col[4] = "90"
        if col[4] == "92" : col[4] = "90"
        if col[4] == "93" : col[4] = "90"
        if col[4] == "94" : col[4] = "90"
        newLine = col[0] + "," + col[1] + "," + col[2] + "," + col[3] + "," + col[4]
        outputList.append(newLine)
    return outputList

def selectPlayer(SelectString, WhereString, dbname):
    outputList = list();
    sql = ""
    conn = None
    try:
        conn = psycopg2.connect("dbname='" + dbname + "' user='myuser' host='localhost' port='65432' password='123qwe'")
        cur = conn.cursor()
        sql = SelectString + "\nFROM player" + WhereString + "\n"
        print(sql)
        
        cur.execute(sql)
        row = cur.fetchone()
        while row is not None:
            #print(row)
            outputList.append(row)
            row = cur.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print(sql)
    finally:
        if conn is not None:
            conn.close()
    return outputList

def renameNumber(inputList, folder, dbname):
    data={}
    SelectString = ""
    SelectString += "\n" + "SELECT "
    SelectString += "\n" + "    num, playerid --01 02 "
    WhereString = ""
    WhereString += "\n" + "WHERE "
    WhereString += "\n" + "    date = '" + folder.replace('/','-') + "' "
    WhereString += "\n" + "    order by num "
    numPlayerIDtupleList = selectPlayer(SelectString, WhereString, dbname)
    for tuple in numPlayerIDtupleList:
        data[str(tuple[1])]=str(tuple[0])
    #print(data)
    #print(data.keys())

    outputList = list();
    for line in inputList:
        col = line.split(",")

        #print(col[1] in data.keys())
        if col[1] in data.keys():
            col[1] = data[col[1]]

        newLine = col[0] + "," + col[1] + "," + col[2] + "," + col[3] + "," + col[4]
        outputList.append(newLine)
    return outputList

def sortByPO(inputList):
    outputList = list();
    inputList, outputList = pickUpByKeyword(inputList, outputList, "KP")
    inputList, outputList = pickUpByKeyword(inputList, outputList, "WB")
    inputList, outputList = pickUpByKeyword(inputList, outputList, "CD")
    inputList, outputList = pickUpByKeyword(inputList, outputList, "W")
    inputList, outputList = pickUpByKeyword(inputList, outputList, "IM")
    inputList, outputList = pickUpByKeyword(inputList, outputList, "FW")

    return outputList

def pickUpByKeyword(inputList, outputList, keyword):
    newInputList = list()
    for i in range(len(inputList)):
        col = inputList[i].split(",")
        if col[0] == keyword:
            outputList.append(col[0] + "," + col[1] + "," + col[2] + "," + col[3] + "," + col[4])
        else:
            newInputList.append(inputList[i])
    return newInputList, outputList

def removeRows(inputList):
    outputList = list();
    for line in inputList:
        col = line.split(",")
        if ( col[0] == "PO" or col[0] == "KP" or col[0] == "WB" or col[0] == "CD" or col[0] == "W" or col[0] == "IM" or col[0] == "FW" ):
            outputList.append(line)
        elif ( col[0] == "-1") :
            print("PO is not changed yet : " + line)
        else :
            print("This line is removed : " + line)
    return outputList

def hasMyPlayer(matchList, playerNumList):
    result = False
    for playerNum in playerNumList:
        for line in matchList:
            col = line.split(",")
            if col[1] == str(playerNum):
                print("playerNum =", playerNum, "matchPlayerNum =", col[1])
                result = True
                break
        else:
            continue
        break
    return result
