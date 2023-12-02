POSSIBLE_BAGS = [
    {
        "red" : 12,
        "green" : 13,
        "blue"  : 14
    }
]

def GetGameResultsFromFile( filename ):
    gameResults = open( filename, 'r' )
    retList = {}
    for gameLine in gameResults:
        gameData = {}
        splitGameLine = gameLine.split( ':' )
        gameID = int( splitGameLine[0].split(' ')[1] )
        for draw in splitGameLine[1].split( ';' ):
            for colourResult in draw.split( ',' ):
                splitColourResult = colourResult.strip().split( ' ' )
                colourName = splitColourResult[1].strip().lower()
                colourCount = int(splitColourResult[0])
                if colourName in gameData and colourCount < gameData[ colourName ]:
                    continue
                gameData[ colourName ] = colourCount
        retList[gameID] = gameData
        
    return retList

def IsPossibleMatch( gameData ):
    print(f'gameData: {gameData}')
    for possibleBag in POSSIBLE_BAGS:
        for draw in gameData.split( ';' ):
            for colourResult in draw.split( ',' ):
                splitColourResult = colourResult.strip().split( ' ' )
                colourName = splitColourResult[1].strip().lower()
                if colourName in possibleBag and possibleBag[ colourName ] < int(splitColourResult[0]):
                    return False
    return True


gameResults = GetGameResultsFromFile( '../InputData/GameResults.txt' )
sum = 0
for gameID in gameResults:
    gameResult = gameResults[gameID]
    #print( gameResult )
    gamePower = 1
    for colour in gameResult:
        gamePower *= gameResult[colour]
    sum += gamePower

print(f'Sum of powers = {sum}')
