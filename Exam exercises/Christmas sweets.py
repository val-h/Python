baklPrice = float(input('Price for baklava/kg - '))
mufPrice = float(input('Price for muffins/kg - '))
shtolenKg = float(input('Shtolen Kg - '))
bonKg = float(input('BonBon Kg - '))
biscKg = float(input('Biscuits Kg - '))

totalPrice = 0.0
#Shtolen - i have no idea what kind of sweet is this
shtolenPrice = baklPrice + baklPrice * 0.6
totalPrice += shtolenKg * shtolenPrice
#BonBon
bonPrice = mufPrice + mufPrice * 0.8
totalPrice += bonPrice * bonKg
#Biscuits
totalPrice += biscKg * 7.5

print(f'Inna needs {totalPrice:.2f}lv for the sweets.')