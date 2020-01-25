n = int(input('Enter the value for n: '))
for i in range(1, 9):
    for q in range(1, 9):
        for j in range(1, 9):
            for u in range(1, 9):
                if n % i == 0 and n % q ==0 and n % j == 0 and n % u == 0:
                    print(f'{i}{q}{j}{u}', end=' ')