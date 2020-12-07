def part1(data):
    with open("06.txt") as f:
        data = f.readlines()
        data = [line.strip() for line in data]
    
    parsedData = parseData(data)
    yesCount = 0
    for i in parsedData:
        yesCount += len(i)

    print(yesCount)
    return yesCount

def part2(data):
    with open("06.txt") as f:
        data = f.readlines()
        data = [line.strip() for line in data]

    parsedData = parseData(data, part=2)
    totalYesCount = 0

    for group in parsedData:
        thisGroupsSets = list()
        for declarationString in group:
            stringSet = set(declarationString)
            thisGroupsSets.append(stringSet)
        
        uniqueLetters = thisGroupsSets[0].copy()
        for declarationSet in thisGroupsSets:
            uniqueLetters.intersection_update(declarationSet)

        groupYesses = len(uniqueLetters)
        totalYesCount += groupYesses

    print(totalYesCount)
    return totalYesCount


def parseData(data, part=1):

    def seperateIntoGroups(data):

        # Add the index of all '' items to a list
        dataSeperators = list()
        for idx, i in enumerate(data):
            if i == '':
                dataSeperators.append(idx)
        seperatorsLength = len(dataSeperators)
        
        # Slice the data in the right positions using the indexes previously found, add new items to a list cotaining all the  (unparsed)
        prev = 0
        allDataPieces = list()
        for i in range(seperatorsLength):
            mySlicedData = data[prev:dataSeperators[i]]
            allDataPieces.append(mySlicedData)
            prev = dataSeperators[i] + 1
        allDataPieces.append(data[prev:])

        return allDataPieces

    allGroups = seperateIntoGroups(data)

    # For each group, break up any strings, and remove all duplicate letters
    allData = list()
    for group in allGroups:       
        
        if part == 1:
            groupDataLength = len(group)
            seperatedLetters = list()
            if groupDataLength == 0:
                for x in group:
                    seperatedLetters.append(x)

            else:
                for x in group:
                    breakLetters = [y for y in x]
                    for z in breakLetters:
                        seperatedLetters.append(z)

                allData.append(set(seperatedLetters))
        
        elif part == 2:
            allData.append(group)

        
    return allData