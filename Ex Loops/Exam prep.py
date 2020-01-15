badGrades = int(input('Bad grades: '))
grdCnt = 0
exercName = None
totalGrade = 0
i = 0
lastExr = None
while grdCnt < badGrades:
    exercName = input('Exercise name: ')
    if exercName == 'Enough':
        break
    grade = float(input('Grade: '))
    totalGrade += grade
    if grade <= 4:
        grdCnt+=1
    i += 1
    lastExr = exercName
totalGrade /= i
if grdCnt == badGrades:
    print(f'You need a break, {grdCnt} poor grades.')
elif exercName == 'Enough':
    print(f'Average score: {totalGrade:.2f}')
    print(f'Number of problems: {i}')
    print(f'Last problem: {lastExr}')