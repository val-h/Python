usrInp = None
kidTickets = 0
stndTickets = 0
studTickets = 0
totalTickets = 0
while True:
    usrInp = input('Enter a command or a Movie: ')
    percFull = 0
    if usrInp == 'Finish':
        break
    tickets = int(input('Enter the number of tickets: '))
    for i in range(1, tickets + 1):
        ticketType = input('Type of ticket: ').lower()
        if ticketType == 'end':
            break
        if ticketType == 'standard':
            stndTickets += 1
        elif ticketType == 'student':
            studTickets += 1
        elif ticketType == 'kid':
            kidTickets += 1
        percFull += 1
        totalTickets += 1
    percFull = percFull / tickets * 100
    print(f'{usrInp} - {percFull:.2f}% full.')
print(f'Total tickets: {totalTickets}.')
print(f'{studTickets / totalTickets * 100:.2f}% student tickets.')
print(f'{stndTickets / totalTickets * 100:.2f}% standard tickets.')
print(f'{kidTickets / totalTickets * 100:.2f}% kids tickets.')
