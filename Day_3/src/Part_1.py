from enum import IntEnum

class SymbolType(IntEnum):
    BLANK = 0
    NUMERIC = 1
    SYMBOL = 2

class ParsedSchematicLine:
    def __init__(self, type, parsedData = None) -> None:
        self.type = type
        self.parsedData = parsedData
        self.counted = False
    def __str__(self) -> str:
        return f'type:{SymbolType(self.type).name}, parsedData:{self.parsedData}, counted:{self.counted}'

def ParseSchematic( filename ):
    schematic = open( filename, 'r' )
    parsedSchematic = []
    for schematicLine in schematic:
        parsedLine = []
        i = 0
        while i < len( schematicLine ) - 1:
            currChar = schematicLine[i]
            if( currChar == '.'):
                parsedLine.append(ParsedSchematicLine(SymbolType.BLANK))
            elif( currChar.isnumeric() ):
                number = ''
                parsedNumber = ParsedSchematicLine(SymbolType.NUMERIC)
                startIndex = i
                while currChar.isnumeric():
                    i = i + 1
                    number += currChar
                    currChar = schematicLine[i]
                parsedNumber.parsedData = number
                for _ in range(startIndex, i):
                    parsedLine.append(parsedNumber)
                continue
            else:
                parsedLine.append(ParsedSchematicLine(SymbolType.SYMBOL))
            i = i + 1
        parsedSchematic.append(parsedLine)
    return parsedSchematic


sum = 0
parsedSchematic = ParseSchematic( '../InputData/Schematic.txt' )

'''for schematicRow in parsedSchematic:
    rowData = ''
    i = 0
    while i < len(schematicRow):
        curentSymbol = schematicRow[i]
        if curentSymbol.type == SymbolType.BLANK:
            rowData += '.'
        elif curentSymbol.type == SymbolType.SYMBOL:
            rowData += '#'
        else:
            rowData += curentSymbol.parsedData
            i += len(curentSymbol.parsedData)-1
        i = i + 1
    print(rowData)'''
        

numRows = len( parsedSchematic )
for i in range( numRows ):
    currRow = parsedSchematic[i]
    for j in range( len( currRow ) ):
        if currRow[j].type == SymbolType.SYMBOL:
            #print(f'Symbol found at ({i}, {j})')
            for iOffset in range(0,3):
                for jOffset in range(0,3):
                    offSetI = i + ( iOffset - 1 )
                    offsetJ = j + ( jOffset - 1 )
                    #print( f'i = {i}, iOffset = {iOffset-1}, j = {j}, jOffset = {jOffset-1}')
                    if offSetI >= 0 and offSetI < numRows and offsetJ >= 0 and offsetJ < len(parsedSchematic[offSetI]):
                        item = parsedSchematic[offSetI][offsetJ]
                        #print(f'({offSetI},{offsetJ}) = {item}')
                        if item.type == SymbolType.NUMERIC and not item.counted:
                            sum += int(item.parsedData)
                            item.counted = True
print(sum)
