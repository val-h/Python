income = float(input())
grade = float(input())
minSal = float(input())
social = bool(0)
excel = bool(0)
socialM = 0.0
excelM = 0.0

if grade > 4.5 and income < minSal:
    social = 1
    socialM = minSal * 0.35
if grade >= 5.5:
    excel = 1
    excelM = grade * 25

if grade < 5.5 or (grade <= 4.5 and income >= minSal):
    print('You cannot get a scholarship!')
elif excel == 1 or social == 1:
    if socialM == excelM or excelM > socialM:
        print(f'You get a scholarship for excellent results {excelM:.2f} BGN')
    else:
        print(f'You get a Social scholarship {socialM:.2f} BGN')