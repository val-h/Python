lineOfProducts = input('Products: ')
lineOfQuantities = input('Quantities: ')
lineOfPrices = input('Prices: ')
products = lineOfProducts.split()
quantities = [int(x) for x in lineOfQuantities.split()]
prices = [float(x) for x in lineOfPrices.split()]

def ProductCost(product, quantity):
    i = products.index(product)
    tempCost = 0
    if i < len(quantities):
        if quantity <= quantities[i]:
            tempCost = quantity * prices[i]
            quantities[i] -= quantity
            return f'{product} x {quantity} costs {tempCost:.2f}'
        else:
            return f'We do not have enough {product}'
    else:
        return f'We do not have enough {product}'

while True:
    cmd = input('/> ')
    if cmd == 'done': break
    tProd, tQuan = cmd.split()
    tQuan = int(tQuan)
    if tProd in products:
        print(ProductCost(tProd, tQuan))
    else:
        print(f'Error. Command {cmd} does not exist.')
