ticketData = open( '../InputData/Tickets.txt', 'r' )

#print(ticketData)

cardResults = []
for ticket in ticketData:
    splitTicket = ticket.split(':')[1].split('|')
    ticketNumbers = splitTicket[0].split()
    playerNumbers = splitTicket[1].split()
    numbersFound = 0
    for playerNumber in playerNumbers:
        if playerNumber in ticketNumbers:
            numbersFound += 1
    cardResults.append(numbersFound)

def GetSum( cardResults ):
    indexesToCheck = list(range(len(cardResults)))
    #print( indexesToCheck )
    for i in indexesToCheck:
        #print( f'{i}: {indexesToCheck}' )
        if i < len(cardResults) and cardResults[i] > 0:
            newIndexes = range( i+1, min( i + cardResults[i] + 1, len(cardResults) ))
            #print(f'{i}: {cardResults[i]} adding indexes {list(newIndexes)}')
            indexesToCheck.extend(newIndexes)
    return len(indexesToCheck)

print(cardResults)

print( f'sum= {GetSum( cardResults )}' )
