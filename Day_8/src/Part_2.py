import math

class Map:
    path = ''
    nodes: dict[str, (str, str)] = {}
    def __init__(self, path: str) -> None:
        self.path = path
    def __str__(self) -> str:
        strData: str = self.path + "\n\n"
        for nodeName in self.nodes:
            strData += f'{nodeName} = ({self.nodes[nodeName][0]}, {self.nodes[nodeName][1]})\n'
        return strData
    def AddNode(self, nodeName: str, leftName: str, rightName: str ):
        self.nodes[nodeName] = (leftName, rightName)
    def GetNextNodeName(self, nodeName: str, dir: str ):
        chosenNode = self.nodes[nodeName]
        if( dir == 'L'):
            return chosenNode[0]
        else:
            return chosenNode[1]

    def GetPathPoint(self, index):
        return self.path[ index % len(self.path) ]


def ParseMap( mapData: list[str] ):
    parsedMap: Map = Map( mapData[0] )
    for line in mapData[2:]:
        splitLine = line.split(' = ')
        splitNodes = splitLine[1].split(', ')
        parsedMap.AddNode( splitLine[0].strip(), splitNodes[0][1:], splitNodes[1][:-1] )
    return parsedMap

InputMap: Map = ParseMap( open( '../InputData/Map.txt' ).read().splitlines() )
currentNodes: list[str] = [ key for key in InputMap.nodes.keys() if key.upper().endswith('A') ]
lengths: list[int] = []
print(InputMap)
print(currentNodes)
foundEnd: bool = False
for nodeName in currentNodes:
    i = 0
    currentNode = nodeName
    while not currentNode.upper().endswith('Z'):
        currentNode = InputMap.GetNextNodeName(currentNode, InputMap.GetPathPoint(i))
        i += 1
    lengths.append( i )
print( lengths )
print( math.lcm(*lengths) )
