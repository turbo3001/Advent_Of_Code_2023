from enum import IntEnum
import itertools

class HandType(IntEnum):
    HIGH_CARD = 0,
    ONE_PAIR = 1,
    TWO_PAIR = 2,
    THREE_OF_A_KIND = 3,
    FULL_HOUSE = 4,
    FOUR_OF_A_KIND = 5,
    FIVE_OF_A_KIND = 6

CARD_ORDER = [ 'J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A' ]

def getCardIndex( card: str ) -> int:
    return CARD_ORDER.index( card )

class Hand:
    def __init__(self, hand, bid) -> None:
        self.hand = hand
        self.bid = int(bid)
        self.handType = self.CalculateHandType()

    def __str__(self) -> str:
        return f'[{self.hand} ({self.GetSortedHand()}) (Type: {HandType(self.handType).name} ({self.handType})) {self.bid}]'
    def __repr__(self) -> str:
        return str(self)
    
    def __lt__(self, other: object) -> bool:
        print(f'comparing {self} to {other}')
        lessThan: bool = False
        if not self.handType == other.handType:
            lessThan = self.handType < other.handType
        else:
            for i in range( len(self.hand) ):
                selfValue = getCardIndex( self.hand[i] )
                otherValue = getCardIndex( other.hand[i] )
                print( f'\t{self.hand[i]} ({selfValue}) vs {other.hand[i]} ({otherValue})' )
                if not selfValue == otherValue :
                    lessThan = selfValue < otherValue
                    break
        print(f'\tlessThan = {lessThan}')
        return lessThan

    def GetSortedHand(self) -> str:
        return str.join( '', sorted( self.hand, key=getCardIndex, reverse=True ) )

    def CalculateHandType(self) -> HandType:
        numJokers = 0
        uniqueCount: dict[str,int] = {}
        for card in self.hand:
            if card == 'J':
                numJokers += 1
                continue
            if card not in uniqueCount:
                uniqueCount[card] = 0
            uniqueCount[card] += 1
        numSets = len(uniqueCount)
        #print(f'{numJokers}, {numSets}, {uniqueCount}')
        if numJokers == 5:
            return HandType.FIVE_OF_A_KIND
        elif numSets == 1:
            return HandType.FIVE_OF_A_KIND
        elif numSets == 2:
            if numJokers == 1 and 2 in uniqueCount.values():
                return HandType.FULL_HOUSE
            elif numJokers >= 1:
                return HandType.FOUR_OF_A_KIND
            elif 4 in uniqueCount.values():
                return HandType.FOUR_OF_A_KIND
            else:
                return HandType.FULL_HOUSE
        elif numSets == 3:
            if 3 in uniqueCount.values():
                if numJokers > 0:
                    return HandType.FOUR_OF_A_KIND
                return HandType.THREE_OF_A_KIND
            elif numJokers > 1:
                return HandType.THREE_OF_A_KIND
            else:
                return HandType.TWO_PAIR
        elif numSets == 4:
            return HandType.ONE_PAIR
        else:
            return HandType.HIGH_CARD



def ParseHands( handData ) -> list[Hand]:
    parsedHands: list[Hand] = []
    for row in handData:
        splitRow = row.split()
        parsedHands.append(Hand(splitRow[0], splitRow[1]))
    return parsedHands

def GenerateTestData(symbols: list[str]) -> list[str]:
    generatedData = [ (''.join(x) + ' 1') for x in itertools.product(symbols, repeat=5)]
    return generatedData


handData = GenerateTestData(CARD_ORDER)
#handData = open( '../InputData/handCraftedHands.txt', 'r' )

allHandsSortedFile = open( '../Output/allHandsSorted.txt','w' )
hands = ParseHands( handData )
hands.sort()
allHandsSortedFile.write(str(hands))
allHandsSortedFile.close()

sum = 0
i = 0
numHands = len(hands)
while i < numHands:
    currentHand: Hand = hands[i]
    handValue: int = (i + 1) * currentHand.bid
    print(f'{i+1}: {currentHand} ({handValue})')
    sum += handValue
    i += 1

print(sum)