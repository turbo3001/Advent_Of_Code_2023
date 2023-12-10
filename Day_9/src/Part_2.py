from collections import deque

class OASIS_Reading:
    def __init__(self, rawData: str) -> None:
        self.readingData: deque[int] = deque(map( int, rawData.split() ))
        self.prediction: int = self.CalculatePrediction()
    
    def __str__(self) -> str:
        return f'[ {self.readingData} -> {self.prediction} ]'
    def __repr__(self) -> str:
        return str(self)

    def CalculatePrediction(self) -> int:
        rows: list[deque[int]] = [self.readingData]
        i = 0
        while not all( reading == 0 for reading in rows[i] ) and i < len(rows):
            newRow: deque = deque()
            j = 1
            while j < len(rows[i]):
                newRow.append( rows[i][j] - rows[i][j-1] )
                j = j + 1
            i = i + 1
            rows.append( newRow )
        i -= 2
        while i >= 0:
            rows[i].appendleft( ( rows[i][0] ) - ( rows[i+1][0] ))
            i -= 1
        #print(rows)
        return rows[0][0]
    
def ParseOASISData( rawOASISData ) -> list[OASIS_Reading]:
    Readings: list[OASIS_Reading] = []
    for dataLine in rawOASISData:
        Readings.append(OASIS_Reading(dataLine))
    return Readings


parsedOASISData: list[OASIS_Reading] = ParseOASISData(open('../InputData/OASIS.txt'))
print(parsedOASISData)
sum = 0
for readingData in parsedOASISData:
    sum += readingData.prediction
print(sum)