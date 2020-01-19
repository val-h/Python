openTabs = int(input('Number of open tabs in the brauser: '))
salary = float(input('Employee salary: '))
for i in range(1, openTabs + 1):
    tab = input(f'Tab {i}: ').lower()
    if tab == 'facebook':
        salary -= 150
    elif tab == 'instagram':
        salary -= 100
    elif tab == 'reddit':
        salary -= 50
    if salary <= 0:
        break
if salary > 0:
    print(f'Salary left: {salary:.2f}')
else:
    print('You have lost your salary. :(')