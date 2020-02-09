lineOfProducts = input('Products: ')
lineOfProductQuantities = input('Quantities: ')
lineOfProductPrices = input('Prices: ')
products = lineOfProducts.split()
productQuantities = [int(x) for x in lineOfProductQuantities.split()]
productPrices = [float(x) for x in lineOfProductPrices.split()]

def ProductInfo(product):
    i = products.index(product)
    print(f'{product} costs {productPrices[i]}; Available quantity: {productQuantities[i]}')


while True:
    cmd = input('/> ')
    if cmd == 'done': break
    if cmd in products:
        ProductInfo(cmd)
    else:
        print(f'Error. Command {cmd} does not exist.')
