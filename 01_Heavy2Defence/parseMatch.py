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

def renamePO(inputList):
    outputList = list();
    for line in inputList:
        col = line.split(",")
        if (col[0] == "0" or col[0] == "114" or col[0] == "118" or col[0] == "119") : col[0] = ""
        if col[0] == "100" : col[0] = "KP"
        if ( col[0] == "101" or col[0] == "105" ) : col[0] = "WB"
        if ( col[0] == "102" or col[0] == "103" or col[0] == "104" ) : col[0] = "CD"
        if ( col[0] == "106" or col[0] == "110" ) : col[0] = "W"
        if ( col[0] == "107" or col[0] == "108" or col[0] == "109" ) : col[0] = "IM"
        if ( col[0] == "111" or col[0] == "112" or col[0] == "113" ) : col[0] = "FW"
        
        if len(col[0]) > 0:
            newLine = col[0] + "," + col[1] + "," + col[2] + "," + col[3] + "," + col[4]
            outputList.append(newLine)

    oldPo=""
    oldNum=""
    oldStartMin=""
    oldEndMin=""
    for i in range(0, len(outputList)):
        col = outputList[i].split(",")
        if col[0] == "-1" and col[3] == oldEndMin:
            col[0] = oldPo
            outputList[i] = col[0] + "," + col[1] + "," + col[2] + "," + col[3] + "," + col[4]
        oldPo = col[0]
        oldNum = col[1]
        oldStartMin = col[3]
        oldEndMin = col[4]

    countOfPo={}
    for i in range(0, len(outputList)):
        col = outputList[i].split(",")
        if col[0] in countOfPo:
            countOfPo[col[0]] += 1
        else:
            countOfPo[col[0]] = 1

    if countOfPo['WB'] == 1 and countOfPo['-1'] == 1:
        for i in range(0, len(outputList)):
            print(i, outputList[i], sep='\t')
        print(countOfPo)
        for i in range(0, len(outputList)):
            col = outputList[i].split(",")
            if col[0] == "-1":
                col[0] = "WB"
                outputList[i] = col[0] + "," + col[1] + "," + col[2] + "," + col[3] + "," + col[4]
        for i in range(0, len(outputList)):
            print(i, outputList[i], sep='\t')

    return outputList

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

def changedPlayer(inputList):
    tmpList = list();
    oldPO = ""
    oldFromMin = ""
    oldToMin = ""
    for line in inputList:
        col = line.split(",")
        if ( oldPO != "CO" and col[0] == "-1" and ( oldFromMin == col[4] or oldToMin == col[3] ) ) :
            col[0] = oldPO
        else :
            oldPO = col[0]
            oldFromMin = col[3]
            oldToMin = col[4]
        newLine = col[0] + "," + col[1] + "," + col[2] + "," + col[3] + "," + col[4]
        tmpList.append(newLine)
    outputList = list();
    oldPO = ""
    oldFromMin = ""
    oldToMin = ""
    for line in reversed(tmpList):
        col = line.split(",")
        if ( oldPO != "CO" and col[0] == "-1" and ( oldFromMin == col[4] or oldToMin == col[3] ) ) :
            col[0] = oldPO
        else :
            oldPO = col[0]
            oldFromMin = col[3]
            oldToMin = col[4]
        newLine = col[0] + "," + col[1] + "," + col[2] + "," + col[3] + "," + col[4]
        outputList.append(newLine)
    lastList = list();
    for line in reversed(outputList):
        lastList.append(line)
    return lastList

def selectPlayer(SelectString, WhereString):
    outputList = list();
    sql = ""
    conn = None
    try:
        conn = psycopg2.connect("dbname='mydatabase2' user='myuser' host='localhost' port='65432' password='123qwe'")
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

def renameNumber(inputList, folder):
    data={}
    SelectString = ""
    SelectString += "\n" + "SELECT "
    SelectString += "\n" + "    num, playerid --01 02 "
    WhereString = ""
    WhereString += "\n" + "WHERE "
    WhereString += "\n" + "    date = '" + folder.replace('/','-') + "' "
    WhereString += "\n" + "    order by num "
    numPlayerIDtupleList = selectPlayer(SelectString, WhereString)
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

def pickUpByKeyword(inputList, outputList, keyword):
    newInputList = list();
    for line in inputList:
        col = line.split(",")
        if col[0] == keyword:
            outputList.append(line)
        else :
            newInputList.append(line)
    return newInputList, outputList

def sortByPO(inputList):
    inputList.sort(key = lambda x: ( x.split(",")[0], -int(x.split(",")[3]), int(x.split(",")[4])))   

    outputList = list();
    outputList.append("po,num,rt,sMin,eMin")

    inputList, outputList = pickUpByKeyword(inputList, outputList, "KP")
    inputList, outputList = pickUpByKeyword(inputList, outputList, "WB")
    inputList, outputList = pickUpByKeyword(inputList, outputList, "CD")
    inputList, outputList = pickUpByKeyword(inputList, outputList, "W")
    inputList, outputList = pickUpByKeyword(inputList, outputList, "IM")
    inputList, outputList = pickUpByKeyword(inputList, outputList, "FW")

    return outputList
