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
