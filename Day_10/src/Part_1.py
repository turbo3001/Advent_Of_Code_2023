import math

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
    

START_DIRS: dict[str, Point] = {
    '|': Point(0, 1),
    '-': Point(1, 0),
    'L': Point(-1, 0),
    'J': Point(1, 0),
    '7': Point(1, 0),
    'F': Point(-1, 0)
}

def getNextDir( type: str, entryDir: Point ) -> Point:
    if type == '|' or type == '-':
        return entryDir
    elif type == 'L' or type == '7':
        return Point( entryDir.y, entryDir.x )
    elif type == 'J' or type == 'F':
        return Point( -entryDir.y, -entryDir.x )
    else:
        raise Exception(f'We\'ve run aground! Found type {type}!')
        
class MazeData:
    def __init__(self, rawData:list[list[str]], startLocation: Point, startChar: str) -> None:
        self.rawData = rawData
        self.startLocation = startLocation
        self.startChar = startChar
    def GetPathLength(self) -> int:
        startDir = START_DIRS[self.startChar]
        currentDir = getNextDir(self.startChar, startDir )
        currentLocation = self.startLocation + currentDir
        length = 0
        print(f'{length} {self.startChar} ({self.startLocation} -> {startDir}) = {currentLocation} -> {currentDir}')
        while currentLocation != self.startLocation:
            prevDir = currentDir
            prevLocation = currentLocation
            if currentLocation.y < 0 or currentLocation.y > len(self.rawData) or currentLocation.x < 0 or currentLocation.x > len(self.rawData[currentLocation.y]):
                raise Exception("We've left the bounds of the data!")
            currentType = self.rawData[currentLocation.y][currentLocation.x]
            currentDir = getNextDir(currentType, currentDir)
            currentLocation += currentDir
            length += 1
            print(f'{length} {currentType} ({prevLocation} -> {prevDir}) = {currentLocation} -> {currentDir}')
        return length


def parseMaze(mazeData: iter ) -> MazeData:
    readData:list[list[str]] = []
    startLocation: Point = Point(-1, -1)
    startChar = ''
    y = 0
    for mazeLine in mazeData:
        # This only works because I manually worked it out and added it to the start of each file. 
        # TODO: Implement a way to work this out automatically
        if startChar == '' and mazeLine.upper().startswith('S'): 
            startChar = mazeLine.split('=')[1]
            continue
        x = 0
        rowData = []
        for type in mazeLine:
            if type.upper() == 'S':
                startLocation = Point( x, y )
            rowData.append(type)
            x += 1
        readData.append(rowData)
        y += 1

    print( readData )
    if startLocation == Point( -1, -1 ):
        raise Exception( 'No Start Location Found!' )

    return MazeData(readData, startLocation, startChar)

parsedMazeData = parseMaze( open('../InputData/Maze.txt', 'r').read().split('\n') )
print( math.ceil( parsedMazeData.GetPathLength()/2 ) )