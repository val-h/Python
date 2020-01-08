budget = float(input())
stat = int(input())
statCl = float(input())
cost = 0.0

cost = budget * 0.1 # decor cost
if stat < 150:
    cost += stat * statCl
else:
    cost += stat * statCl - stat * statCl * 0.1

if budget >= cost:
    print('Action!')
    print(f'Wingard starts filming with {budget - cost:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {cost - budget:.2f} leva more.')