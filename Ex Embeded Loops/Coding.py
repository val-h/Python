# Definetly has a better way of doing it but still works
n = int(input('Enter a number to encrypt: '))
for i in str(n):
    lastDig = int(n % 10)
    if lastDig == 0:
        print('ZERO')
    else:        
        for j in range(0, lastDig):
            print(chr(lastDig + 33), end='')
        print()
    n /= 10