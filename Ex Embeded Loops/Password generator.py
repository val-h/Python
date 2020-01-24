n = int(input('Enter a value for n: '))
l = int(input('Enter a value for l: '))
chrStart = 97
chrStop = 97 + l
for i in range(1, n):
    for j in range(1, n):
        for q in range(chrStart, chrStop):
            for u in range(chrStart, chrStop):
                for y in range(j+1, n +1):
                    print(f'{i}{j}{chr(q)}{chr(u)}{y}', end=' ')
