start = int(input('Number to start from: '))
finish = int(input('Number to finish at: '))
magicNum = int(input('Magical number: '))
cnt, x1, x2 = 0, 0, 0
extEmbeded = False # not so elegant
# > for i looP:
#   second if i + q:     - this is mroe elgant but is not practical if the condition
#       break               is inexpensive to compute
for i in range(start, finish + 1):
    for q in range(start, finish + 1):
        cnt += 1
        if i + q == magicNum:
            x1 = i
            x2 = q
            extEmbeded = True
            break
    if extEmbeded == True:
        break
if x1 + x2 == magicNum:
    print(f'Combination N: {cnt} ({x1} + {x2} = {magicNum})')
else:
    print(f'{cnt} combinations - neither equals {magicNum}')

#   Searching for an elegant way to exit embeded loop was too time consuming : (