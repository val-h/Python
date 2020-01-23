completeAverageGrade = 0
juryMembers = int(input('How many members are in the jury? - '))
numOfPresentations = 0
while True:
    cmd = input('>> ')
    if cmd == 'Finish':
        break
    pScore = 0.0
    for i in range(0, juryMembers):
        juryScore = float(input(f'Jury {i + 1} - '))
        pScore += juryScore
    pScore = pScore / juryMembers
    completeAverageGrade += pScore
    numOfPresentations += 1
    print(f'{cmd} - {pScore:.2f}.')
completeAverageGrade = completeAverageGrade / numOfPresentations
print(f'Student\'s final assessment is {completeAverageGrade:.2f}')
