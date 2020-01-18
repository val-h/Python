age = int(input('Age: '))
wmPrice = float(input('WashingMachine price: '))
toyPrice = float(input('Price for a single toy: '))
moneyRecieved = 10
savings = 0.0
for i in range( 1, age + 1):
    if i % 2 != 0:
        savings += toyPrice
    else:
        savings += moneyRecieved
        moneyRecieved += 10
        savings -= 1 # scummy brother stealing them moneyz
if savings >= wmPrice:
    print(f'Yes! {savings - wmPrice:.2f}')
else:
    print(f'No! {wmPrice - savings:.2f}')