badGrades = int(input'Bad grades: ')
grdCnt = 0
exercName = None
while grdCnt < badGrades:
    exercName = input('Exercise name: ')
    grade = float(input('Grade: '))
    if grade < 4:
        grdCnt+=1
if grdCnt >= badGrades:
    pass #todo finish this