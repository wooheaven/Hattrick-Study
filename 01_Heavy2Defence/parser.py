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
