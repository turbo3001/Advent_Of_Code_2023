POSSIBLE_BAGS = [
    {
        "red" : 12,
        "green" : 13,
        "blue"  : 14
    }
]

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


gameResults = open( '../InputData/GameResults.txt', 'r' )
matchingGames = []
for gameLine in gameResults:
    print( gameLine )
    gameData = gameLine.split( ':' )
    if IsPossibleMatch( gameData[1] ):
        matchingGames.append( int(gameData[0].split(' ')[1]) )

print( f'Matching Games: {', '.join( map(str, matchingGames) )}' )
print( f'Sum of Matching Game IDs { sum( matchingGames ) }' )
