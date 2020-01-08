days = float(input())
bakers = float(input())
cakes = float(input())
gof = float(input())
pancakes = float(input())

totalSum = float(bakers * days * ((cakes * 45) + (gof * 5.8) + (pancakes * 3.2)))
totalSum-= totalSum * (1 / 8) # 0.125

print(f'{totalSum:.2f} lv.')