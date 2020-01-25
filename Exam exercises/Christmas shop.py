target = float(input('Organizers required target: '))
fantasyBooks = int(input('The number of Fantasy books sold: '))
horrorBooks = int(input('The number of Horror books sold: '))
romanceBooks = int(input('The number of Romance books sold: '))

totalSum = 0.0
# Types of books sold
totalSum += fantasyBooks * 14.9
totalSum += horrorBooks * 9.80
totalSum += romanceBooks * 4.30
# Taxes - 20%
totalSum -= totalSum * 0.2
# Employee bonuses if the target is met
employeeBonus = 0.0
if totalSum > target:
    employeeBonus = totalSum - target
    employeeBonus = int(employeeBonus * 0.1)
    totalSum -= employeeBonus
    print(f'{totalSum:.2f}lv donated. Sellers will receive {employeeBonus} leva.')
else:
    print(f'{target - totalSum:.2f} leva needed.')
