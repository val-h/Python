n = int(input('Integer: '))

def PrintSign(num):
    if num == 0:
        return 'zero'
    elif num > 0:
        return 'positive'
    else:
        return 'negative'

print(f'The number {n} is {PrintSign(n)}.')
