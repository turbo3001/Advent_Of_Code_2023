from enum import IntEnum

class HandType(IntEnum):
    HIGH_CARD = 0,
    ONE_PAIR = 1,
    TWO_PAIR = 2,
    THREE_OF_A_KIND = 3,
    FULL_HOUSE = 4,
    FOUR_OF_A_KIND = 5,
    FIVE_OF_A_KIND = 6

CARD_ORDER = [ '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A' ]

class Hand:
    def __init__(self, hand, bid) -> None:
        self.hand = hand
        self.bid = int(bid)
        self.handType = self.CalculateHandType()

    def __str__(self) -> str:
        return f'[{self.hand} {self.bid}]'
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self, other: object) -> bool:
        return self.hand.lower() == other.hand.lower()
    def __lt__(self, other: object) -> bool:
        for i in range( len(self.hand) ):
            if not self.handType == other.handType:
                return self.handType < other.handType
            
            selfValue = CARD_ORDER.index( self.hand[i] )
            otherValue = CARD_ORDER.index( other.hand[i] )
            if not selfValue == otherValue :
                return selfValue < otherValue
        return False

    def CalculateHandType(self) -> HandType:
        uniqueCount: dict[str,int] = {}
        for card in self.hand:
            if card not in uniqueCount:
                uniqueCount[card] = 0
            uniqueCount[card] += 1
        numSets = len(uniqueCount)
        if numSets == 1:
            return HandType.FIVE_OF_A_KIND
        elif numSets == 2:
            if 4 in uniqueCount.values():
                return HandType.FOUR_OF_A_KIND
            else:
                return HandType.FULL_HOUSE
        elif numSets == 3:
            if 3 in uniqueCount.values():
                return HandType.THREE_OF_A_KIND
            else:
                return HandType.TWO_PAIR
        elif numSets == 4:
            return HandType.ONE_PAIR
        else:
            return HandType.HIGH_CARD



def ParseHands( filename ) -> list[Hand]:
    handData = open( filename, 'r' )
    parsedHands: list[Hand] = []
    for row in handData:
        splitRow = row.split()
        parsedHands.append(Hand(splitRow[0], splitRow[1]))
    return parsedHands


hands = ParseHands('../InputData/Hands.txt')
hands.sort()
print(hands)

sum = 0
i = 0
numHands = len(hands)
while i < numHands:
    currentHand: Hand = hands[i]
    print(f'{i}: {currentHand}')
    sum += (i + 1) * currentHand.bid
    i += 1

print(sum)