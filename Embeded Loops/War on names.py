usrInp = None
maxPoints = 0
Winner = None
while True:
    usrInp = input('Write a name: ')
    if usrInp == 'STOP':
        break
    tempPoints = 0
    for a in usrInp:
        tempPoints += ord(a)
    if maxPoints < tempPoints:
        Winner = usrInp
        maxPoints = tempPoints
print(f'Winner is {Winner} - {maxPoints}!')