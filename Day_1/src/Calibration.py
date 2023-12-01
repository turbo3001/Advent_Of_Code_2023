PART2_MODE = True

NUMBERS_AS_STRING = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

def FindNumbersInString( inputLine ):
    numbersInString = []
    for index in range(len(inputLine)):
        if( inputLine[index].isnumeric() ):
            numbersInString.append( int(inputLine[index]) )
            continue
        if( PART2_MODE ):
            for numberIndex in range( len( NUMBERS_AS_STRING ) ):
                number = NUMBERS_AS_STRING[numberIndex].lower()
                currentCheck = inputLine[ index : index + len( number ) ]
                if( currentCheck == number ):
                    numbersInString.append(numberIndex)
                    index += len(number)
    return numbersInString

inputdata = open( '../InputData/input.txt', 'r' )
sum = 0
for inputLine in inputdata:
    numbersInLine = FindNumbersInString( inputLine )
    lineNumber = ( numbersInLine[0] * 10 ) +  numbersInLine[-1]
    sum += lineNumber
    print( f'{inputLine[:-1]}\n\tfound numbers { ', '.join( map( str, numbersInLine ) ) }\n\tso lineNumber is {lineNumber}\n\trunning total: {sum}' )
print(f'The calibration value is {sum}')