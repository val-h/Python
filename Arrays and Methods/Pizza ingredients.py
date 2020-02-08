ingredients = input('Ingredients: ')
arrIngredients = ingredients.split()
charIngredient = int(input('Specific lenght: '))
arrAdded = []
addedIngr = 0


for i in range(0, len(arrIngredients)):
    if charIngredient == len(arrIngredients[i]):
        if addedIngr == 10: break
        print(f'Adding {arrIngredients[i]}.')
        arrAdded.append(arrIngredients[i])
        addedIngr += 1

if addedIngr > 0:
    print(f'Made pizza with total of {addedIngr} ingredients.')
    print(f'The ingredients are: ', end='')
    for i in range(0, len(arrAdded)):
        if i == len(arrAdded) - 1:
            print(arrAdded[i], end='.\n')
        else:
            print(arrAdded[i], end=', ')
