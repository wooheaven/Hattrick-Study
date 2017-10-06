def removeHattrickTag(inputList):
    outputList = list();
    for line in inputList:
        if line.find('table') == -1:
            line = line.replace('[tr]', '')
            line = line.replace('[/tr]', '')
            line = line.replace('[th]', '')
            line = line.replace('[/th]', ',')
            line = line.replace('[td]', '')
            line = line.replace('[/td]', ',')
            outputList.append(line)
    return outputList

def combineTwoLine(inputList):
    outputStr = "";
    for line in inputList:
        col = line.split(",")
        #print(len(col), line, sep="\t")
        if len(col) == 37 : 
            outputStr = outputStr + line + "\n"
        if len(col) == 5 : 
            outputStr = outputStr + line 
        if len(col) == 33 : 
            for i in range(1, 33):
                outputStr = outputStr + "," + col[i]
            outputStr = outputStr + "\n"
    outputStr = outputStr[:-1]
    return outputStr.split("\n")

def modifySharpToNumber(inputList):
    outputList = list();
    for line in inputList:
        if line.find("#") > -1 : line = line.replace("#", "Number")
        outputList.append(line)
    return outputList

def modifySpToSpecial(inputList):
    outputList = list();
    for line in inputList:
        if line.find("Sp") > -1 : 
            line = line.replace("Sp", "Special", 1)
        else :
            line = line.replace("공 마술사", "Technical", 1)
            line = line.replace("빠름", "Quick", 1)
            line = line.replace("헤딩", "Head", 1)
            line = line.replace("힘", "Powerful", 1)
            line = line.replace("예측할 수 없음", "Unpredictable", 1)
        outputList.append(line)
    return outputList

def removeFirstColumn(inputList):
    outputList = list();
    for line in inputList:
        col = line.split(",")
        tmpStr = ""
        
        for i in range(1,len(col)):
            tmpStr += col[i] + ","
        tmpStr = tmpStr[:-1]
        outputList.append(tmpStr)
    return outputList

def dividePlayerAndPlayerID(inputList):
    outputList = list();
    for line in inputList:
        col = line.split(",")
        tmpStr = ""
        if col[2] == "Player": 
            col[2] = "Player,PlayerID"
            tmpStr += col[0]
            for i in range(1, len(col)):
                tmpStr += "," + col[i]
            outputList.append(tmpStr)
        else : 
            tmpStr = col[2].replace(" [playerid=", ",", 1)
            endIndex = tmpStr.find("]")
            col[2] = tmpStr[:endIndex]
            
            tmpStr = col[0]
            for i in range(1, len(col)):
                tmpStr += "," + col[i]
            outputList.append(tmpStr)
    return outputList

from datetime import datetime
from dateutil.relativedelta import relativedelta
import re

class SeasonWeekDay:
    
    def __init__(self, timeStr):
        for myStr in timeStr.split(' '):
            if ( re.search('시즌', myStr) ):
                self.seasonInt = int(myStr[:-2])
            if ( re.search('주', myStr) ):
                self.weekInt = int(myStr[:-1])
            if ( re.search('일', myStr) ):
                self.dayInt = int(myStr[:-1])
    
    def display(self):
        outStr = ''
        if (hasattr(self, 'seasonInt')):
            if (self.seasonInt > 0):
                outStr += str(self.seasonInt) + '시즌 '
        if (hasattr(self, 'weekInt')):
            outStr += str(self.weekInt) + '주 '
        if (hasattr(self, 'dayInt')):
            outStr += str(self.dayInt) + '일'
        return outStr
    
    def modify(self, diffDayInt):
        if (self.dayInt >= diffDayInt):
            self.dayInt = self.dayInt - diffDayInt
        else :
            if (self.weekInt > 0):
                self.weekInt -= 1
                self.dayInt = self.dayInt - diffDayInt + 7
            else :
                if (self.weekInt == 0):
                    self.seasonInt -= 1
                    self.weekInt = 15
                    self.dayInt = self.dayInt - diffDayInt + 7

def modifySince(inputList, targetStr, nowStr):   
    outputList = list();
    for line in inputList:
        col = line.split(",")
        if col[7] != "Since":            
            col[7] = col[7].replace(" 시즌", "시즌", 1).replace("시즌 ", "시즌", 1).replace("시즌 ", "시즌", 1)
            col[7] = col[7].replace(" 주", "주", 1).replace("주 ", "주", 1).replace("주 ", "주", 1)
            col[7] = col[7].replace(" 일", "일", 1)
            
            targetDay = datetime.strptime(targetStr, '%Y/%m/%d').date()
            nowDay = datetime.strptime(nowStr, '%Y/%m/%d').date()
            diffDay = relativedelta(nowDay, targetDay)
            
	    #print(col[7])

            modifySinceStr = SeasonWeekDay(col[7])
            modifySinceStr.modify(int(diffDay.days))
            
            print(int(diffDay.days), col[7], modifySinceStr.display())
            col[7] = modifySinceStr.display()
            
            tmpStr = col[0]
            for i in range(1, len(col)):
                tmpStr += "," + col[i]
            
            outputList.append(tmpStr)
        else:
            outputList.append(line)
    return outputList

def modifyMB(inputList):
    outputList = list();
    for line in inputList:
        col = line.split(",")
        if col[14] == "MB":
            outputList.append(line)
        if len( col[14] ) == 1:
            tmpLine = line.replace("✔", "TRUE", 1)
            outputList.append(tmpLine)
        if len( col[14] ) == 0:
            col[14] = "FALSE"
            tmpLine = col[0]
            for i in range(1, len(col) ):
                tmpLine += "," + col[i]
            outputList.append(tmpLine)
    return outputList

def modifyLast(inputList):
    outputList = list();
    for line in inputList:
        col = line.split(",")
        if col[23] == "Last":
            outputList.append(line)
        else :
            col[23] = col[23][:10]
            tmpLine = col[0]
            for i in range(1, len(col)):
                tmpLine += "," + col[i]
            outputList.append(tmpLine)
    return outputList

def assignEmptyForTC(inputList):
    outputList = list();
    for line in inputList:
        col = line.split(",")
        if col[28] == "TC":
            outputList.append(line)
        else :
            col[28] = ""
            tmpLine = col[0]
            for i in range(1, len(col)):
                tmpLine += "," + col[i]
            outputList.append(tmpLine)
    return outputList

def assignEmptyForPH(inputList):
    outputList = list();
    for line in inputList:
        col = line.split(",")
        if col[29] == "PH":
            outputList.append(line)
        else :
            col[29] = ""
            tmpLine = col[0]
            for i in range(1, len(col)):
                tmpLine += "," + col[i]
            outputList.append(tmpLine)
    return outputList

def modifyKPPos(inputList):
    outputList = list();
    for line in inputList:
        col = line.split(",")
        if col[30] == "KP": 
            col[30] = "KPPos"
            tmpLine =col[0]
            for i in range(1, len(col)):
                tmpLine += "," + col[i]
            outputList.append(tmpLine)
        else :
            outputList.append(line)
    return outputList

def modifyWBPos(inputList):
    outputList = list();
    for line in inputList:
        col = line.split(",")
        if col[31] == "WB": 
            col[31] = "WBPos"
            tmpLine =col[0]
            for i in range(1, len(col)):
                tmpLine += "," + col[i]
            outputList.append(tmpLine)
        else :
            outputList.append(line)
    return outputList

def modifyCDPos(inputList):
    outputList = list();
    for line in inputList:
        col = line.split(",")
        if col[32] == "CD": 
            col[32] = "CDPos"
            tmpLine =col[0]
            for i in range(1, len(col)):
                tmpLine += "," + col[i]
            outputList.append(tmpLine)
        else :
            outputList.append(line)
    return outputList

def modifyWPos(inputList):
    outputList = list();
    for line in inputList:
        col = line.split(",")
        if col[33] == "W": 
            col[33] = "WPos"
            tmpLine =col[0]
            for i in range(1, len(col)):
                tmpLine += "," + col[i]
            outputList.append(tmpLine)
        else :
            outputList.append(line)
    return outputList

def modifyIMPos(inputList):
    outputList = list();
    for line in inputList:
        col = line.split(",")
        if col[34] == "IM": 
            col[34] = "IMPos"
            tmpLine =col[0]
            for i in range(1, len(col)):
                tmpLine += "," + col[i]
            outputList.append(tmpLine)
        else :
            outputList.append(line)
    return outputList

def modifyFWPos(inputList):
    outputList = list();
    for line in inputList:
        col = line.split(",")
        if col[35] == "FW": 
            col[35] = "FWPos"
            tmpLine =col[0]
            for i in range(1, len(col)):
                tmpLine += "," + col[i]
            outputList.append(tmpLine)
        else :
            outputList.append(line)
    return outputList

def removeLastString(inputList):
    outputList = list();
    for line in inputList:
        outputList.append( line[0:-1] )
    return outputList


