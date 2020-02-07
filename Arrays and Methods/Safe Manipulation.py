words = input('Input of words: ')
arrWords = words.split()
cmd = None

def Distinct(arr):
    uniqueArr = []
    for i in range(0, len(arr)):
        if arr[i] not in uniqueArr:
            uniqueArr.append(arr[i])
    return uniqueArr

def Replace(i, word):
    arrWords[i] = word
    return arrWords
    

while True:
    cmd = input('/> ')
    if cmd == 'END': break
    if cmd == 'Reverse':
        arrWords.reverse()
    elif cmd == 'Distinct':
        arrWords = Distinct(arrWords)
    else:
        tempArr = cmd.split()
        if tempArr[0] == 'Replace':
            index = int(tempArr[1])
            if index < 0 or index >= len(arrWords):
                print('Invalid Input')
            else:
                wRep = tempArr[2]
                arrWords = Replace(index, wRep)
        else:
            print('Error. Command doesn\'t exist.')

for output in range(0, len(arrWords)):
    print(f'{arrWords[output]}, ', end='')
