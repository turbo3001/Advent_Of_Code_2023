ticketData = open( '../InputData/Tickets.txt', 'r' )

#print(ticketData)

sum = 0
for ticket in ticketData:
    splitTicket = ticket.split(':')[1].split('|')
    ticketNumbers = splitTicket[0].split()
    playerNumbers = splitTicket[1].split()
    #print(f'{ticketNumbers}')
    numbersFound = 0
    for playerNumber in playerNumbers:
        if playerNumber in ticketNumbers:
            #print(f'Found {playerNumber} in ticket ({numbersFound})')
            numbersFound += 1
    if numbersFound > 0:
        #print(f'found {numbersFound} numbers, adding {2 ** ( numbersFound - 1 )} to sum')
        sum += ( 2 ** ( numbersFound - 1 ) )

print( sum )
