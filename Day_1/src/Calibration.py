inputdata = open( '../InputData/input.txt', 'r' )
sum = 0
for inputLine in inputdata:
    numbersInLine = []
    for character in inputLine:
        if( character.isnumeric() ):
            numbersInLine.append( int(character) )
    lineNumber = ( numbersInLine[0] * 10 ) +  numbersInLine[-1]
    sum += lineNumber
    print( f'{inputLine[:-1]} = {lineNumber} (running total: {sum})' )
print(f'The calibration value is {sum}')
