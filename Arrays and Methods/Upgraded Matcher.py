lineOfProducts = input('Products: ')
lineOfQuantities = input('Quantities: ')
lineOfPrices = input('Prices: ')
products = lineOfProducts.split()
quantities = [int(x) for x in lineOfQuantities.split()]
prices = [float(x) for x in lineOfPrices.split()]

def ProductCost(product):
    i = products.index(product)
    if i < len(quantities): # Finish this
        print('Yes')
    else:
        print('No')

while True:
    cmd = input('/> ')
    if cmd == 'done': break
    if cmd in products:
        ProductCost(cmd)
    else:
        print(f'Error. Command {cmd} does not exist.')
