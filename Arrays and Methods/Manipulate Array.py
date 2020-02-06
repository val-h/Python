words = input('Input of words: ')
arrWords = words.split()
countCmd = int(input('Number of commands to be executed: '))

def Distinct(arr):
    uniqueArr = []
    for i in range(0, len(arr)):
        if arr[i] not in uniqueArr:
            uniqueArr.append(arr[i])
    return uniqueArr

def Replace(i, word):
    arrWords[i] = word
    return arrWords
    

for i in range(0, countCmd):
    cmd = input('/> ')
    if cmd == 'Reverse':
        arrWords.reverse()
    elif cmd == 'Distinct':
        arrWords = Distinct(arrWords)
    else:
        tempArr = cmd.split()
        if tempArr[0] == 'Replace':
            index = int(tempArr[1])
            wRep = tempArr[2]
            arrWords = Replace(index, wRep)
        else:
            print('Error. Command doesn\'t exist.')

for output in range(0, len(arrWords)):
    print(f'{arrWords[output]}, ', end='')
