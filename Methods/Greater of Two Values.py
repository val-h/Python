inpType = input('Input type: ').lower()
first = input('First value: ')
second = input('Second value: ')

def MaxInput(f, s):
    if inpType == 'int':
        f, s = int(f), int(s)
        return max(f, s)
    elif inpType == 'string' or inpType == 'char':
        return max(f, s)
    else:
        return 'Error'

print(MaxInput(first, second))
