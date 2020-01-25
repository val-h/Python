#   User input
competitionStage = input('Stage: ').lower()
ticketType = input('Type of the ticket: ').lower()
amountOfTickets = int(input('Amount of tickets: '))
pictureWithTrophy = input('Picture with trophy: ')

#   Variables
totalSum = 0.0
error = False

#   Total cost calculation
if competitionStage == 'quarter final':
    if ticketType == 'standard':    totalSum = amountOfTickets * 55.5
    elif ticketType == 'premium':   totalSum = amountOfTickets * 105.2
    elif ticketType == 'vip':   totalSum = amountOfTickets * 118.9
    else:   error = True      
elif competitionStage == 'semi final':
    if ticketType == 'standard':    totalSum = amountOfTickets * 75.88
    elif ticketType == 'premium':   totalSum = amountOfTickets * 125.22
    elif ticketType == 'vip':   totalSum = amountOfTickets * 300.40
    else:   error = True      
elif competitionStage == 'final':
    if ticketType == 'standard':    totalSum = amountOfTickets * 110.10
    elif ticketType == 'premium':   totalSum = amountOfTickets * 160.66
    elif ticketType == 'vip':   totalSum = amountOfTickets * 400
    else:   error = True
else:   error = True

#   Discounts
if totalSum > 4000:    totalSum -= totalSum * 0.25
elif totalSum > 2500:
    totalSum -= totalSum * 0.1
    if pictureWithTrophy == 'Y':   totalSum += amountOfTickets * 40
elif pictureWithTrophy == 'Y':   totalSum += amountOfTickets * 40

#   Output
print(f'Total cost for the tickets: {totalSum:.2f}')
