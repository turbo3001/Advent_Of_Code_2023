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
    def GetNextNodeName(self, nodeName, dir ):
        chosenNode = self.nodes[nodeName]
        if( dir == 'L'):
            return chosenNode[0]
        else:
            return chosenNode[1]
    def GetPathPoint(self, index):
        return self.path[ index % len(self.path) ]


def ParseMap( mapData: list[str] ):
    map: Map = Map( mapData[0] )
    for line in mapData[2:]:
        splitLine = line.split(' = ')
        splitNodes = splitLine[1].split(', ')
        map.AddNode( splitLine[0].strip(), splitNodes[0][1:], splitNodes[1][:-1] )
    return map

map: Map = ParseMap( open( '../InputData/Map.txt' ).read().splitlines() )
currentNode: str = 'AAA'
i = 0
while not currentNode.upper() == 'ZZZ'.upper():
    currentNode = map.GetNextNodeName(currentNode, map.GetPathPoint(i))
    i += 1

print(i)
