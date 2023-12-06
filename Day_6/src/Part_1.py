class Race():
    def __init__(self, time, distance) -> None:
        self.time = int(time)
        self.distance = int(distance)
    def __str__(self) -> str:
        return f'[time: {self.time}, distance: {self.distance}]'
    def __repr__(self) -> str:
        return str(self)
    def GetWinningDistanceCount(self) -> int:
        count = 0
        i = 0
        while i < self.time:
            if i * (self.time - i) > self.distance:
                count += 1
            i = i + 1
        return count

def parseRaces( filename ) -> list[Race]:
    races = []
    raceInfo = {}
    for row in open( filename, 'r' ):
        splitRow = row.split( ':' )
        raceInfo[ splitRow[0] ] = splitRow[1].split()
    for i in range( len(raceInfo['Time']) ):
        races.append( Race( raceInfo['Time'][i], raceInfo['Distance'][i] ) )
    return races

races = parseRaces( '../InputData/RaceTimes.txt' )
print(races)
sum = 1
for race in races:
    sum *= race.GetWinningDistanceCount()

print(sum)