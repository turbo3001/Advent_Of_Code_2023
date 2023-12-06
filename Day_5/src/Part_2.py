import math

class MappingEntry():
    def __init__(self, destRangeStart, srcRangeStart, length) -> None:
        self.srcRangeStart = int(srcRangeStart)
        self.destRangeStart = int(destRangeStart)
        self.length = int(length)
    def __str__(self) -> str:
        return f'src: [{self.srcRangeStart} -> {self.srcRangeStart + self.length-1}], dest: [{self.destRangeStart} -> {self.destRangeStart + self.length-1}]'
    def __repr__(self) -> str:
        return str(self)
    def GetDestFromSrc(self, src):
        src = int(src)
        if src < self.srcRangeStart or src >= self.srcRangeStart + self.length:
            return -1
        #print(f'(srcRangeStart: {self.srcRangeStart} destRangeStart: {self.destRangeStart} length: {self.length}): GetDestFromSrc({src}) index = {( self.srcRangeStart - src ) + self.length}')
        return self.destRangeStart + ( src - self.srcRangeStart )

class SeedRange():
    def __init__(self, startIndex, length) -> None:
        self.startIndex = int(startIndex)
        self.endIndex = self.startIndex + int(length)
    def __str__(self) -> str:
        return f'[{self.startIndex} -> {self.endIndex}]'
    def __repr__(self) -> str:
        return str(self)

class Almanac():
    def __init__(self) -> None:
        self.seedList = []
        self.mapping = {
            'soil': [],
            "fertilizer": [],
            "water": [],
            "light": [],
            "temperature": [],
            "humidity": [],
            "location": []
        }
    
    def __str__(self) -> str:
        return f'Seeds: {self.seedList}\nMappings:{self.mapping}'
    
    def AddSeed( self, seedNumber ) -> None:
        if seedNumber not in self.seedList:
            self.seedList.append( seedNumber )

    def AddMapping(self, type, mapping) -> None:
        if not isinstance(mapping, MappingEntry):
            return
        self.mapping[type].append( mapping )

    def GetMappings( self, type ) -> list:
        return self.mapping[type]
        

def ParseAlmanac( filename ):
    almanacData = open(filename, 'r')
    almanac = Almanac()
    currentType = ''
    for almanacLine in almanacData:
        lineData = almanacLine.split(':')
        #print(f'parsing: {almanacLine}')
        if len(lineData) > 1:
            if lineData[0] == "seeds":
                seedData = lineData[1].split()
                i = 0
                while i < len(seedData)-1:
                    start = int(seedData[i])
                    length = int(seedData[i+1])
                    #print(f'i={i}, start={int(seedData[i])}, length = {int(seedData[i+1])}')
                    almanac.AddSeed(SeedRange(start, length))
                    i += 2
            else:
                currentType = lineData[0].split(' ')[0].split('-')[2] #This is nasty
            continue
        elif len(lineData[0].strip()) > 0:
            mappingData = lineData[0].split()
            almanac.AddMapping( currentType, MappingEntry(mappingData[0], mappingData[1], mappingData[2]) )
    return almanac
        
         
almanac = ParseAlmanac('../InputData/Almanac.txt')

print(almanac)

lowestLocation = math.inf
for seed in almanac.seedList:
    i = seed.startIndex
    while i < seed.endIndex:
        currentSrc = i
        for mappingKey in almanac.mapping:
            initialSrc = currentSrc
            for mapping in almanac.GetMappings(mappingKey):
                newDest = mapping.GetDestFromSrc(currentSrc)
                if newDest >= 0:
                    currentSrc = newDest
                    break
            #print(f'{i} {mappingKey}: [{initialSrc}] -> [{currentSrc}]')
        if currentSrc < lowestLocation:
            lowestLocation = currentSrc
        i += 1

print(lowestLocation)