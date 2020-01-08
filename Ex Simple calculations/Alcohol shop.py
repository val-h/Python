whiskey = float(input())
lBeer = float(input())
lWine = float(input())
lRakia = float(input())
lWhiskey = float(input())

rakiaPrice = whiskey / lWhiskey / 2
winePrice = rakiaPrice * 0.6
beerPrice = rakiaPrice * 0.2

rakia = lRakia * rakiaPrice
wine = lWine * winePrice
beer = lBeer * beerPrice

sum = whiskey + rakia + wine + beer

print(f'{sum:.2f} lv.')