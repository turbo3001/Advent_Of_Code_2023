class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return f'({self.x}, {self.y})'
    def __repr__(self) -> str:
        return str(self)
    
    def __add__(self, other):
        return Point( self.x + other.x, self.y + other.y )

    def __eq__(self, __value: object) -> bool:
        return self.x == __value.x and self.y == __value.y


def ParseGalaxyImage( imageData: iter ):
    galaxyData: list[list[str]] = []
    filledColumns: list[int] = []
    j = 0
    for row in imageData:
        galaxyData.append(list(row))
        if not any( [x for x in row if x == '#'] ):
            #print(f'Expanding row {j}')
            galaxyData.append(list(row))
        else:            
            for i in range(len(row)):
                if row[i] == '#' and i not in filledColumns:
                    filledColumns.append(i)
        j += 1
    
    #filledColumns.sort()
    numColumns = len(galaxyData[0])
    emptyColumns = [x for x in range(numColumns) if x not in filledColumns]
    #print(f'Found Galaxies in the following Columns: {','.join(map(str, filledColumns))}\nEmpty Columns found: {','.join(map(str, emptyColumns))}')

    expandedColumnCount = 0
    for i in emptyColumns:
        #print(f'Expanding Column {i+expandedColumnCount}')
        for j in range(len(galaxyData)):
            galaxyData[j].insert(i+expandedColumnCount, '.')
        expandedColumnCount += 1
    #print(f'Expanded {expandedColumnCount} columns')

    return galaxyData

galaxyImage = ParseGalaxyImage( open('../InputData/Image.txt').read().split('\n') )
sum = 0
foundLocs:list[Point] = []
for row in range(len(galaxyImage)):
    for column in range(len(galaxyImage[row])):
        if galaxyImage[row][column] == '#':
            #print(f'Found Galaxy at ({column}, {row})')
            foundLocs.append( Point(column, row) )


'''for row in galaxyImage:
    print(''.join(row))'''
    
numLocs = len(foundLocs)
for i in range(numLocs):
    currentPoint = foundLocs[i]
    j = i+1
    while j < numLocs:
        comparePoint = foundLocs[j]
        distance = 0
        if currentPoint.x > comparePoint.x:
            distance += currentPoint.x - comparePoint.x
        else:
            distance += comparePoint.x - currentPoint.x

        if currentPoint.y > comparePoint.y:
            distance += currentPoint.y - comparePoint.y
        else:
            distance += comparePoint.y - currentPoint.y
         
        #print(f'Distance between {i+1} and {j+1} is {distance}')
        sum += distance
        j += 1

'''numRows = len(galaxyImage)
rowLength = len(galaxyImage[0])
numSymbols = numRows * rowLength
for i in range( numSymbols ):
    positionInRow = i % rowLength
    rowNumber = i - positionInRow
    currentSymbol = galaxyImage[rowNumber][positionInRow]
    if currentSymbol == '#':
        j = i
        while j < numSymbols:
            jPositionInRow = j % rowLength
            jRowNumber = j - positionInRow
            if galaxyImage[jRowNumber][jPositionInRow] == '#':
                sum += (jPositionInRow - positionInRow) + (jRowNumber - rowNumber)'''
print(sum)

