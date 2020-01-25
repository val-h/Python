#   User input
speaker = int(input('Cost for speaker: '))

#   Variables
guestSum = 0
totalGuests = 0
usrInp = None

#   Loop
while True:
    usrInp = input('Enter the number of people in the group: ')
    if usrInp == 'The restaurant is full':  break
    groupCount = int(usrInp)
    if groupCount < 5:  guestSum += groupCount * 100
    else:   guestSum += groupCount * 70
    totalGuests += groupCount

#   Output
if guestSum >= speaker:   print(f'You have {totalGuests} guests and {guestSum - speaker} leve left.')
else:   print(f'You have {totalGuests} guests and {guestSum} leva income, but no singer.')
