import re

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
        if col[0] == "0" : col[0] = "CO"
        if col[0] == "100" : col[0] = "KP"
        if ( col[0] == "101" or col[0] == "105" ) : col[0] = "WB"
        if ( col[0] == "102" or col[0] == "103" or col[0] == "104" ) : col[0] = "CD"
        if ( col[0] == "106" or col[0] == "110" ) : col[0] = "W"
        if ( col[0] == "107" or col[0] == "109" ) : col[0] = "IM"
        if ( col[0] == "111" or col[0] == "112" or col[0] == "113" ) : col[0] = "FW"
        
        newLine = col[0] + "," + col[1] + "," + col[2] + "," + col[3] + "," + col[4]
        outputList.append(newLine)
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
        #PO,Number,Star,FromMin,ToMin
        #FW,17, 4.5,38,90
        #-1,16,-1.0, 0,38
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
        #PO,Number,Star,FromMin,ToMin
        # IM,26,5.0,40,90
        # -1,11,-1.0,0,40
        # W,22,4.0,0,50
        # -1,24,-1.0,50,90
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

