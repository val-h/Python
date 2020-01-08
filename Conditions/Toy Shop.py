hPrice = float(input('Holiday price: '))
cntPuzzels = int(input('Puzzels: '))
cntDolls = int(input('Dools: '))
cntBears = int(input('Bears: '))
cntTrucks = int(input('Trucks: '))
cntMinnions = int(input('Minnions: '))

money = 0.0
toysCnt = cntPuzzels + cntDolls + cntTrucks + cntBears + cntMinnions

money += cntPuzzels * 2.60
money += cntDolls * 3
money += cntBears * 4.10
money += cntTrucks * 8.20
money += cntMinnions * 2

print(money)

if toysCnt >= 50:
    money -= money * 0.25
money -= money * 0.1
print(money)

if money >= hPrice:
    print(f'Yes! {money - hPrice:.2f} lv left.')
else:
    print(f'Not enough money! {hPrice - money:.2f} lv needed.')