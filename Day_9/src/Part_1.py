class OASIS_Reading:
    def __init__(self, rawData: str) -> None:
        self.readingData: list[int] = list(map( int, rawData.split() ))
        self.prediction: int = self.CalculatePrediction()
    
    def __str__(self) -> str:
        return f'[ {self.readingData} -> {self.prediction} ]'
    def __repr__(self) -> str:
        return str(self)

    def CalculatePrediction(self) -> int:
        rows: list[list[int]] = [self.readingData]
        i = 0
        while not all( reading == 0 for reading in rows[i] ) and i < len(rows):
            newRow = []
            j = 1
            while j < len(rows[i]):
                newRow.append( rows[i][j] - rows[i][j-1] )
                j = j + 1
            i = i + 1
            rows.append( newRow )
        #print(rows)
        i -= 2
        while i >= 0:
            rows[i].append( ( rows[i][len(rows[i]) - 1] ) + ( rows[i+1][len(rows[i+1]) - 1] ))
            i -= 1
        return rows[0][ len( rows[0] ) - 1 ]
    
def ParseOASISData( rawOASISData ) -> list[OASIS_Reading]:
    Readings: list[OASIS_Reading] = []
    for dataLine in rawOASISData:
        Readings.append(OASIS_Reading(dataLine))
    return Readings


parsedOASISData: list[OASIS_Reading] = ParseOASISData(open('../InputData/OASIS.txt'))
sum = 0
for readingData in parsedOASISData:
    sum += readingData.prediction
print(sum)